// Redux is a predictable state container for JavaScript apps.

// Rule1: Only an event can change the state of the store.
// Rule2: The function that returns the new state needs to be a pure function.

// Object.assign(target, sources.....)

// Actions: Recoreds of state change.
// Action Creators: functions that create/return action objects
/*
Action Creator:
const addItem = item => ({
  type: ADD_ITEM,
  item
});

Action:
{
  type: ADD_ITEM,
  item
}
*/


/*

What are Pure Functions?
Pure functions are integral to how state in Redux applications is updated.
By definition, pure functions:

    -Return the same result if the same arguments are passed in
    -Depend solely on the arguments passed into them
    -Do not produce side effects, such as API requests and I/O operations

So, the pure function will be the Reducer, because its role to
take a (CurrentState, Action) and return (NewSate).

NewState = Reducer(CurrentState, Action)

CurrentState = Action Tree.

The Reducer Must be PUER FUNCTION.


*/

function createStore(reducer) {
  // The store should have four parts
  // 1. The state
  // 2. Get the state.
  // 3. Listen to changes on the state.
  // 4. Update the state

  let state;

  let listeners = [];

  // returns the state.
  const getState = () => state

  // listens for change.
  const subscribe =
      (listener) => {
        listeners.push(listener)
        // Run function if want to remove specific listener.
        return () => {
          listeners = listeners.filter((l) => l !== listener)
        }
      }

  // Update the State.
  const dispatch =
      (action) => {
        // NewState = Reducer(CurrentState, Action)
        state = reducer(state, action)
        listeners.forEach((listener) => listener())
      }

  return {
    getState, subscribe, dispatch
  }
}


const ADD_TODO = 'ADD_TODO'
const REMOVE_TODO = 'REMOVE_TODO'
const TOGGLE_TODO = 'TOGGLE_TODO'
const ADD_GOAL = 'ADD_GOAL'
const REMOVE_GOAL = 'REMOVE_GOAL'

// Action Creators
function addTodo(todo) {
  return {
    type: ADD_TODO, todo
  }
}

function removeTodo(id) {
  return {
    type: REMOVE_TODO, id
  }
}

function toggleTodo(id) {
  return {
    type: TOGGLE_TODO, id
  }
}

function removeGoal(id) {
  return {
    type: REMOVE_GOAL, id
  }
}

function addGoal(goal) {
  return {
    type: ADD_GOAL, goal
  }
}


function todos(state = [], action) {
  switch (action.type) {
    case ADD_TODO:
      return state.concat([action.todo]);

    case REMOVE_TODO:

      return state.filter((s) => s.id !== action.id);

    case TOGGLE_TODO:

      return state.map(
          (todo) => todo.id === action.id ?
              todo :
              Object.assign({}, todo, {complete: !todo.complete}));
    default:
      return state;
  }
}

function goals(state = [], action) {
  switch (action.type) {
    case ADD_GOAL:
      return state.concat([action.goal]);

    case REMOVE_GOAL:

      return state.filter((goal) => goal.id !== action.id);
    default:
      return state;
  }
}

function app(state = {}, action) {
  return {
    todos: todos(state.todos, action), goals: goals(state.goals, action)
  }
}

const store = createStore(app)


const unsubscribe =
    store.subscribe(() => {console.log('The new state is: ', store.getState())})
// unsubscribe()

store.dispatch(addTodo({id: 0, name: 'Learn Redux', complete: true}))
store.dispatch(addTodo({id: 1, name: 'Read Book', complete: false}))
store.dispatch(addGoal({id: 1, name: 'Win Match', complete: false}))
