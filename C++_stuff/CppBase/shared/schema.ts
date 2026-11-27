import { sql } from "drizzle-orm";
import { pgTable, text, varchar, integer, real, timestamp } from "drizzle-orm/pg-core";
import { createInsertSchema } from "drizzle-zod";
import { z } from "zod";

export const users = pgTable("users", {
  id: varchar("id").primaryKey().default(sql`gen_random_uuid()`),
  username: text("username").notNull().unique(),
  password: text("password").notNull(),
});

export const locations = pgTable("locations", {
  id: varchar("id").primaryKey().default(sql`gen_random_uuid()`),
  x: integer("x").notNull(),
  y: integer("y").notNull(),
  createdAt: timestamp("created_at").defaultNow().notNull(),
});

export const locationFiles = pgTable("location_files", {
  id: varchar("id").primaryKey().default(sql`gen_random_uuid()`),
  filename: text("filename").notNull(),
  content: text("content").notNull(),
  processedAt: timestamp("processed_at").defaultNow().notNull(),
});

export const compilationResults = pgTable("compilation_results", {
  id: varchar("id").primaryKey().default(sql`gen_random_uuid()`),
  sourceCode: text("source_code").notNull(),
  compileOutput: text("compile_output"),
  runOutput: text("run_output"),
  success: integer("success").notNull().default(0), // 0 = false, 1 = true
  compiledAt: timestamp("compiled_at").defaultNow().notNull(),
});

export const insertUserSchema = createInsertSchema(users).pick({
  username: true,
  password: true,
});

export const insertLocationSchema = createInsertSchema(locations).pick({
  x: true,
  y: true,
});

export const insertLocationFileSchema = createInsertSchema(locationFiles).pick({
  filename: true,
  content: true,
});

export const insertCompilationResultSchema = createInsertSchema(compilationResults).pick({
  sourceCode: true,
  compileOutput: true,
  runOutput: true,
  success: true,
});

export type InsertUser = z.infer<typeof insertUserSchema>;
export type User = typeof users.$inferSelect;

export type InsertLocation = z.infer<typeof insertLocationSchema>;
export type Location = typeof locations.$inferSelect;

export type InsertLocationFile = z.infer<typeof insertLocationFileSchema>;
export type LocationFile = typeof locationFiles.$inferSelect;

export type InsertCompilationResult = z.infer<typeof insertCompilationResultSchema>;
export type CompilationResult = typeof compilationResults.$inferSelect;
