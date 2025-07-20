import json
from pathlib import Path

class PerspectiveExplorer:
    def __init__(self, topic: str, source_config_path: str = "data/sources.json"):
        self.topic = topic
        self.source_config = self.load_source_config(source_config_path)
        self.exploration_plan = []

    def load_source_config(self, path):
        if not Path(path).exists():
            raise FileNotFoundError(f"Source config not found at {path}")
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def plan_exploration(self):
        self.exploration_plan = []
        for source in self.source_config["sources"]:
            strategy = f"Search '{source['name']}' for '{self.topic}' using {source['method']}"
            self.exploration_plan.append({
                "source": source["name"],
                "method": source["method"],
                "strategy": strategy,
            })
        return self.exploration_plan

    def run(self):
        print(f"[Agent] Exploring topic: '{self.topic}'")
        plan = self.plan_exploration()
        for step in plan:
            print(f"→ {step['strategy']}")
