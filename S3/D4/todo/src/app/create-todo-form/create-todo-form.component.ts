import { Component } from '@angular/core';

export interface ITodo {
  id: string;
  title: string;
  description: string;
  status: boolean;
}

@Component({
  selector: 'app-create-todo-form',
  templateUrl: './create-todo-form.component.html',
  styleUrls: ['./create-todo-form.component.css']
})
export class CreateTodoFormComponent {

  title = ''
  description = ''

  getTodos(): ITodo[] {
    return JSON.parse(localStorage.getItem('todos') as string);
  }

  addTodo(): void {
    const todos = this.getTodos() || [];

    const newTodo: ITodo = {
      id: crypto.randomUUID(),
      title: this.title,
      description: this.description,
      status: false
    };

    todos.push(newTodo);
    localStorage.setItem('todos', JSON.stringify(todos));
  }
}
