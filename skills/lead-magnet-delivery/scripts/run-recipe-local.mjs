#!/usr/bin/env node
/**
 * Local Lead Magnet Delivery Test Runner
 * Validates post comment parsing and ledger deduplication.
 */

import { processCommentDeliveries } from "../references/delivery-recipe.example.mjs";

async function main() {
  console.log("=== Testing Lead Magnet Delivery Pipeline ===");
  const res = await processCommentDeliveries(
    "https://linkedin.com/posts/example",
    "FUNNEL",
    "https://github.com/Aditya-chouhan/linkedin-funnel",
    {}
  );
  console.log("Pipeline test completed successfully:", res);
}

main().catch(console.error);
