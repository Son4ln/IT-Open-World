<?php

namespace App\Http\Controllers\API\Generic;

use Illuminate\Http\Request;
use App\Http\Controllers\Controller;
use Illuminate\Pagination\LengthAwarePaginator;
use Exception;
class APIController extends Controller
{
    /**
     * A Generic controller for API
     */
    protected $request = NULL;
    # $model is a string of model | example "App\Users"
    protected $model = NULL;
    # validator_class is laravel Validator class
    protected $validator_class = NULL;
    # default paginator for api
    protected $paginate = false;
    # paginate_per_page for paginayte
    protected $paginate_per_page = 2;

    function __construct(Request $request) {
        // $this->check_validator_variable();
        $this->check_model_variable();
        $this->request = $request;
    }

    protected function get_model_class() {
        /**
         * Get default model class, and logic code for model here
        */
        return $this->model;
    }

    protected function get_validator_class() {
        /**
         * Get validator class, and logic code for validator here
        */
        return $this->validator_class;
    }

    protected function get_queryset() {
        /**
         * Get default queryset, and logic code for query database here
        */
        return $this->get_model_class()::all();
    }

    protected function paginate_queryset($queryset = NULL) {
        /**
         * Default paginate for api
         */
        if($this->paginate) {
            $queryset = $queryset == NULL ? $this->get_queryset() : $queryset;
            // dd($queryset->toArray());
            return new LengthAwarePaginator($queryset->toArray(), count($queryset->toArray()), $this->paginate_per_page, 1);
        }
        return $this->get_queryset();
    }

    // protected function index() {
    //     return response()->json(
    //         [
    //             "data" => $this->get_queryset(),
    //             "message" => __('messages.created')
    //         ], 200);
    // }

    protected function check_model_variable() {
        if(!$this->model) {
            throw new Exception('Missing model, Please declare the model ');
        }
    }

    protected function check_validator_variable() {
        if(!$this->validator_class) {
            throw new Exception('Missing validator, Please declare the validator_class ');
        }
    }

    // /**
    //  * Display a listing of the resource.
    //  *
    //  * @return \Illuminate\Http\Response
    //  */
    // public function index()
    // {
    //     //
    // }

    // /**
    //  * Store a newly created resource in storage.
    //  *
    //  * @param  \Illuminate\Http\Request  $request
    //  * @return \Illuminate\Http\Response
    //  */
    // public function store(Request $request)
    // {
    //     //
    // }

    // /**
    //  * Display the specified resource.
    //  *
    //  * @param  int  $id
    //  * @return \Illuminate\Http\Response
    //  */
    // public function show($id)
    // {
    //     //
    // }

    // /**
    //  * Update the specified resource in storage.
    //  *
    //  * @param  \Illuminate\Http\Request  $request
    //  * @param  int  $id
    //  * @return \Illuminate\Http\Response
    //  */
    // public function update(Request $request, $id)
    // {
    //     //
    // }

    // /**
    //  * Remove the specified resource from storage.
    //  *
    //  * @param  int  $id
    //  * @return \Illuminate\Http\Response
    //  */
    // public function destroy($id)
    // {
    //     //
    // }
}
