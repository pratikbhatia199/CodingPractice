echo "---------------Correct test case: Skip deals that with start_date >= checkin date ------------------"
echo "python HotelDeals.py ./test_case_files/deals.csv "Hotel CommonWealth" 2014-06-02 3"
python HotelDeals.py ./test_case_files/deals.csv "Hotel CommonWealth" 2014-06-02 3

echo "---------------Correct test case: Skip rebate_3plus deals in date range but stay <3------------------"
echo "python HotelDeals.py ./test_case_files/deals_skip_rebate_plus3.csv "Hotel CommonWealth" 2014-06-30 2"
python HotelDeals.py ./test_case_files/deals_skip_rebate_plus3.csv "Hotel CommonWealth" 2014-06-30 2

echo "------------- Correct test case: Skip deals with end_date <= checkin date -----------------"
echo "python HotelDeals.py ./test_case_files/deals.csv "Hotel CommonWealth" 2015-06-30 2"
python HotelDeals.py ./test_case_files/deals.csv "Hotel CommonWealth" 2015-06-30 2

echo "------------- Boundary case: Skip deals with end_date == checkin date -----------------"
echo "python HotelDeals.py ./test_case_files/deals_boundary_checkin_equals_end.csv "Hotel CommonWealth" 2014-06-15 4"
python HotelDeals.py ./test_case_files/deals_boundary_checkin_equals_end.csv "Hotel CommonWealth" 2014-06-15 4


echo "------------- Boundary case: Include deals with start_date == checkin date -----------------"
echo "python HotelDeals.py ./test_case_files/deals_boundary_start_equals_checkin.csv "Hotel CommonWealth" 2014-07-07 4"
python HotelDeals.py ./test_case_files/deals_boundary_start_equals_checkin.csv "Hotel CommonWealth" 2014-07-07 4

echo "################### Bad Input data ###########################"
echo "--------------File Not found ----------------------"
echo "python HotelDeals.py ./test_case_files/not_found.csv "Hotel CommonWealth" 2014-06-30 3"
python HotelDeals.py ./test_case_files/not_found.csv "Hotel CommonWealth" 2014-06-30 3

echo "--------------Extra Command Line arguments---------"
echo "python HotelDeals.py ./test_case_files/not_found.csv "Hotel CommonWealth" 2014-06-30 3 5"
python HotelDeals.py ./test_case_files/not_found.csv "Hotel CommonWealth" 2014-06-30 3 5

echo "--------------Missing Command Line arguments---------"
echo "python HotelDeals.py ./test_case_files/not_found.csv "Hotel CommonWealth" 2014-06-30"
python HotelDeals.py ./test_case_files/not_found.csv "Hotel CommonWealth" 2014-06-30

echo "--------------Columns Missing in file-----"
echo "python HotelDeals.py ./test_case_files/deals_missing_cols.csv "Hotel CommonWealth" 2014-06-30 3"
python HotelDeals.py ./test_case_files/deals_missing_cols.csv "Hotel CommonWealth" 2014-06-30 3

echo "--------------Extra Columns in file-------"
echo "python HotelDeals.py ./test_case_files/deals_extra_cols.csv "Hotel CommonWealth" 2014-06-30 3"
python HotelDeals.py ./test_case_files/deals_extra_cols.csv "Hotel CommonWealth" 2014-06-30 3

echo "############## Handling Blank Values ##################"

echo "---------------Blank hotel name ----------------------"
echo "python HotelDeals.py ./test_case_files/deals_blank_hotel_name.csv  "Hotel CommonWealth" 2014-06-30 3"
python HotelDeals.py ./test_case_files/deals_blank_hotel_name.csv  "Hotel CommonWealth" 2014-06-30 3


echo "---------------Blank Nightly Rate ----------------------"
echo "python HotelDeals.py ./test_case_files/deals_blank_nightly_rate.csv "Hotel CommonWealth" 2014-06-30 3"
python HotelDeals.py ./test_case_files/deals_blank_nightly_rate.csv "Hotel CommonWealth" 2014-06-30 3

echo "---------------Blank Promotion Text ----------------------"
echo "python HotelDeals.py ./test_case_files/deals_blank_promo.csv "Hotel CommonWealth" 2014-06-30 3"
python HotelDeals.py ./test_case_files/deals_blank_promo.csv "Hotel CommonWealth" 2014-06-30 3

echo "---------------Blank Deal Value ----------------------"
echo "python HotelDeals.py ./test_case_files/deals_blank_deal_value.csv "Hotel CommonWealth" 2014-06-30 3"
python HotelDeals.py ./test_case_files/deals_blank_deal_value.csv "Hotel CommonWealth" 2014-06-30 3

echo "---------------Blank Deal Type ----------------------"
echo "python HotelDeals.py ./test_case_files/deals_blank_deal_type.csv "Hotel CommonWealth" 2014-06-30 3"
python HotelDeals.py ./test_case_files/deals_blank_deal_type.csv "Hotel CommonWealth" 2014-06-30 3

echo "---------------Blank Start date ----------------------"
echo "python HotelDeals.py ./test_case_files/deals_blank_start_date.csv "Hotel CommonWealth" 2014-06-30 3"
python HotelDeals.py ./test_case_files/deals_blank_start_date.csv "Hotel CommonWealth" 2014-06-30 3

echo "---------------Blank End date ----------------------"
echo "python HotelDeals.py ./test_case_files/deals_blank_end_date.csv "Hotel CommonWealth" 2014-06-30 3"
python HotelDeals.py ./test_case_files/deals_blank_end_date.csv "Hotel CommonWealth" 2014-06-30 3


echo "############# Handling Mistakes in Command Line Arguments ###########"
echo "-------- Stay days is not a number ---------------------"
echo "python HotelDeals.py ./test_case_files/deals_blank_end_date.csv "Hotel CommonWealth" 2014-06-30 X"
python HotelDeals.py ./test_case_files/deals_blank_end_date.csv "Hotel CommonWealth" 2014-06-30 X


echo "----------Invalid check in date-------------------------"
echo "python HotelDeals.py ./test_case_files/deals_blank_end_date.csv "Hotel CommonWealth" 2014-62-30 3"
python HotelDeals.py ./test_case_files/deals_blank_end_date.csv "Hotel CommonWealth" 2014-62-30 3


echo "-----------Number of stay days < 1-------------"
echo "python HotelDeals.py ./test_case_files/deals_blank_end_date.csv "Hotel CommonWealth" 2014-06-30 0"
python HotelDeals.py ./test_case_files/deals_blank_end_date.csv "Hotel CommonWealth" 2014-06-30 0

echo "############# Handling Mistakes in File Values ###########"
echo "----------- Invalid start date format --------"
echo "python HotelDeals.py ./test_case_files/deals_invalid_start_date.csv "Hotel CommonWealth" 2014-06-30 4"
python HotelDeals.py ./test_case_files/deals_invalid_start_date.csv "Hotel CommonWealth" 2014-06-30 4


echo "----------- Invalid end date format --------"
echo "python HotelDeals.py ./test_case_files/deals_invalid_end_date.csv "Hotel CommonWealth" 2014-06-30 4"
python HotelDeals.py ./test_case_files/deals_invalid_end_date.csv "Hotel CommonWealth" 2014-06-30 4

echo "----------- Invalid Sequence of start date and end date --------"
echo "python HotelDeals.py ./test_case_files/deals_invalid_start_date_end_date_sequence.csv "Hotel CommonWealth" 2014-06-30 4"
python HotelDeals.py ./test_case_files/deals_invalid_start_date_end_date_sequence.csv "Hotel CommonWealth" 2014-06-30 4

echo "---------- Deal Value >=0 -------------"
echo "python HotelDeals.py ./test_case_files/deals_value_non_negative.csv "Hotel CommonWealth" 2014-06-30 4"
python HotelDeals.py ./test_case_files/deals_value_non_negative.csv "Hotel CommonWealth" 2014-06-30 4


echo "--------- Deal Type invalid ------------"
echo "python HotelDeals.py ./test_case_files/deals_rebate_type_invalid.csv "Hotel CommonWealth" 2014-06-30 4"
python HotelDeals.py ./test_case_files/deals_rebate_type_invalid.csv "Hotel CommonWealth" 2014-06-30 4







