import { Component } from '@angular/core';
import { ITodo } from '../create-todo-form/create-todo-form.component';

@Component({
  selector: 'app-todo-list',
  templateUrl: './todo-list.component.html',
  styleUrls: ['./todo-list.component.css']
})
export class TodoListComponent {

  todos = this.getTodos()

  getTodos(): ITodo[] {
    return JSON.parse(localStorage.getItem('todos') as string);
  }
}
