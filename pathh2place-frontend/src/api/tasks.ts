export async function getTodayTasks(token: string) {
  const res = await fetch("http://localhost:8000/api/tasks/today", {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  if (!res.ok) {
    throw new Error("Failed to fetch tasks");
  }

  return res.json();
}