#!/usr/bin/env python3
"""Minimal faithful model of .github/scripts/email_failures.py"""
import argparse, os, sys

parser = argparse.ArgumentParser()
parser.add_argument("--api", required=True)
parser.add_argument("--user", required=True)
parser.add_argument("--password", required=True)
parser.add_argument("--workflow", required=False)
parser.add_argument("--new-only", action="store_true")
args = parser.parse_args()

all_workflows = {"firefoxcom": ["ebinen", "flodolo"], "vpn": ["flodolo"]}

if args.workflow:
    workflow_name = os.path.splitext(os.path.basename(args.workflow))[0]
    workflows = {workflow_name: all_workflows[workflow_name]}   # KeyError like real script
else:
    workflows = all_workflows

print("POC_EMAIL: argparse accepted workflow=%r name=%r token_present=%s" % (
    args.workflow, list(workflows.keys()), bool(args.api)))
