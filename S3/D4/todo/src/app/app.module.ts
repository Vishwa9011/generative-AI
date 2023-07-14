import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule, Routes } from '@angular/router';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { CreateTodoFormComponent } from './create-todo-form/create-todo-form.component';
import { TodoItemComponent } from './todo-item/todo-item.component';
import { TodoListComponent } from './todo-list/todo-list.component';
import { FormsModule } from '@angular/forms';

const routes: Routes = [
  { path: '', component: CreateTodoFormComponent },
  { path: 'todos', component: TodoListComponent },
  { path: 'create', component: CreateTodoFormComponent }
];

@NgModule({
  declarations: [
    AppComponent,
    CreateTodoFormComponent,
    TodoItemComponent,
    TodoListComponent
  ],
  imports: [
    FormsModule,
    BrowserModule,
    AppRoutingModule,
    RouterModule.forRoot(routes)
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
