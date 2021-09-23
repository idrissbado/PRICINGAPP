from modulesClass.Pricing import Pricing
from modulesClass.Quotation import Quotation
from modulesClass.Basis import Basis
from modulesClass.CommSpouse import CommSpouse
from modulesClass.Commutation import Commutation
from modulesClass.Commexpense import Commexpense
from tools.fonctions import *
from tools.filesConfig import *
from flask import Blueprint, jsonify, request, redirect, url_for
from app import oidc, _logger
import logging

REQUEST_API = Blueprint('request_api', __name__)


@REQUEST_API.route('/')
def index():
    if oidc.user_loggedin:
        return 'Logged In Home Page. <a href="/logout">Logout</a>'
    else:
        return redirect(url_for('REQUEST_API.login'))


@REQUEST_API.route('/login')
@oidc.require_login
def login():
    _logger.info(
        '{} logged in successfully'.format(oidc.user_getfield('email')))
    return redirect(url_for('REQUEST_API.index'))


@REQUEST_API.route('/logout')
@oidc.require_login
def logout():
    email = oidc.user_getfield('email')
    oidc.logout()
    redirect_url = request.url_root.strip('/')
    keycloak_issuer = oidc.client_secrets.get('issuer')
    keycloak_logout_url = '{}/protocol/openid-connect/logout'.format(
        keycloak_issuer
    )
    _logger.info('{} logged out'.format(email))

    return redirect('{}?redirect_uri={}'.format(
        keycloak_logout_url,
        redirect_url)
    )


def get_blueprint():
    """Return the blueprint for the main app module"""
    return REQUEST_API

#quotation--------------------------------------------------------------------------->
@REQUEST_API.route('/quotation/<string:_fonctionName>', methods=['GET','POST'])
@oidc.require_login
def quotation(_fonctionName):

    arguments = request.json

    result = Quotation(ApplicationDate = convertDateTime(arguments.get('ApplicationDate')),
        ClientDateofBirth = convertDateTime(arguments.get('ClientDateofBirth')),
        SpouseDateofBirth = convertDateTime(arguments.get('SpouseDateofBirth')), 
        Inv_Return = float(arguments.get('Inv_Return')), Escal_Rate = float(arguments.get('Escal_Rate')),
        Adj_disc_R = float(arguments.get('Adj_disc_R')), AnnuityFreq = float(arguments.get('AnnuityFreq')), 
        Annuity = float(arguments.get('Annuity')))

    #essential instructions
    print(result.ClientAgeLastBirthday())
    print(result.SpouseAgeLastBirthday())
    print(result.SpouseAgeDifference())
    print(result.AdjustedDiscountRatetouse())
    print(result.MonthlyAdjustedDiscountRatetouse())
    print(result.ModalAnnuity())

    if(_fonctionName == 'ClientAgeLastBirthday'):
        return jsonify({ 'ClientAgeLastBirthday' : result.ClientAgeLastBirthday() })
    if(_fonctionName == 'SpouseAgeLastBirthday'):
        return jsonify({ 'SpouseAgeLastBirthday' : result.SpouseAgeLastBirthday() })
    if(_fonctionName == 'SpouseAgeDifference'):
        return jsonify({ 'SpouseAgeDifference' : result.SpouseAgeDifference() })
    if(_fonctionName == 'AdjustedDiscountRatetouse'):
        return jsonify({ 'AdjustedDiscountRatetouse' : result.AdjustedDiscountRatetouse() })
    if(_fonctionName == 'MonthlyAdjustedDiscountRatetouse'):
        return jsonify({ 'MonthlyAdjustedDiscountRatetouse' : result.MonthlyAdjustedDiscountRatetouse() })
    if(_fonctionName == 'ModalAnnuity'):
        return jsonify({ 'ModalAnnuity' : result.ModalAnnuity() })
    if(_fonctionName == 'quotation'):
        return jsonify({
        'ClientAgeLastBirthday' : result.ClientAgeLastBirthday(),
        'SpouseAgeLastBirthday' : result.SpouseAgeLastBirthday(),
        'SpouseAgeDifference' : result.SpouseAgeDifference(),
        'AdjustedDiscountRatetouse' : result.AdjustedDiscountRatetouse(),
        'MonthlyAdjustedDiscountRatetouse' : result.MonthlyAdjustedDiscountRatetouse(),
        'ModalAnnuity' : result.ModalAnnuity(),
    }) 


#Basis--------------------------------------------------------------------------->
@REQUEST_API.route('/basis/<string:_fonctionName>', methods=['GET','POST'])
@oidc.require_login
def basis(_fonctionName):
    
    arguments = request.json
    
    result = Basis(MarketGrossyieldRate = float(arguments.get('MarketGrossyieldRate')), 
        ReinvestmentRiskMargin = float(arguments.get('ReinvestmentRiskMargin')), 
        PrudentMargin = float(arguments.get('PrudentMargin')),
        Tax = float(arguments.get('Tax')), AnnuityFreq = float(arguments.get('AnnuityFreq')), 
        Expl_Inf_Rate = float(arguments.get('Expl_Inf_Rate')), Enterpremiun = float(arguments.get('Enterpremiun')), 
        PremiumBreak1 = float(arguments.get('PremiumBreak1')), aun = float(arguments.get('aun')),
        PremiumBreak2 = float(arguments.get('PremiumBreak2')), adeux = float(arguments.get('adeux')), 
        atrois = float(arguments.get('atrois')), 
        WritingAgentCommission = float(arguments.get('WritingAgentCommission')),
        UnitManagerComm = float(arguments.get('UnitManagerComm')), 
        AgencyManagerComm = float(arguments.get('AgencyManagerComm')), 
        RegionalManagerComm = float(arguments.get('RegionalManagerComm')),
        DeputyNationalManager = float(arguments.get('DeputyNationalManager')), 
        NationalManagerComm = float(arguments.get('NationalManagerComm')), 
        Illiquiditymargin = float(arguments.get('Illiquiditymargin')),
        Profitcriterion = float(arguments.get('Profitcriterion')))

    if(_fonctionName == 'PricingGrossYieldRate'):
        return jsonify({ 'PricingGrossYieldRate' : result.PricingGrossYieldRate() })
    if(_fonctionName == 'Mthlyconvertibleinvestmentreturnrate'):
        return jsonify({ 'Mthlyconvertibleinvestmentreturnrate' : result.Mthlyconvertibleinvestmentreturnrate() })
    if(_fonctionName == 'AdjustedInflationRate'):
        return jsonify({ 'AdjustedInflationRate' : result.AdjustedInflationRate() })
    if(_fonctionName == 'Monthlyconvertibleadjustedinterestrate'):
        return jsonify({ 'Monthlyconvertibleadjustedinterestrate' : result.Monthlyconvertibleadjustedinterestrate() })
    if(_fonctionName == 'MortalityLoadingAdjustment'):
        return jsonify({ 'MortalityLoadingAdjustment' : result.MortalityLoadingAdjustment() })
    if(_fonctionName == 'Commissionrate'):
        return jsonify({ 'Commissionrate' : result.Commissionrate() })
    if(_fonctionName == 'Naicomlevy'):
        return jsonify({ 'Naicomlevy' : result.Naicomlevy() })
    if(_fonctionName == 'ProfitandContigencyMargin'):
        return jsonify({ 'ProfitandContigencyMargin' : result.ProfitandContigencyMargin() })
    if(_fonctionName == 'basis'):
        return jsonify({
        'PricingGrossYieldRate' : result.PricingGrossYieldRate(),
        'Mthlyconvertibleinvestmentreturnrate' : result.Mthlyconvertibleinvestmentreturnrate(),
        'AdjustedInflationRate' : result.AdjustedInflationRate(),
        'Monthlyconvertibleadjustedinterestrate' : result.Monthlyconvertibleadjustedinterestrate(),
        'MortalityLoadingAdjustment' : result.MortalityLoadingAdjustment(),
        'Commissionrate' : result.Commissionrate(),
        'Naicomlevy' : result.Naicomlevy(),
        'ProfitandContigencyMargin' : result.ProfitandContigencyMargin()
    }) 


#CommSpouse--------------------------------------------------------------------------->
@REQUEST_API.route('/commspouse/<string:_fonctionName>', methods=['GET','POST'])
@oidc.require_login
def commSpouse(_fonctionName):
    
    arguments = request.json
    
    result = CommSpouse(arguments.get('sex'), float(arguments.get('client_age_last_birthday')), float(arguments.get('Adj_disc_R')), float(arguments.get('Guar_period')),Male,Female)

    if(_fonctionName == 'table'):
        return jsonify({ 'table' : result.table().to_json(orient='records').replace('"', '') })
    if(_fonctionName == 'axy'):
        return jsonify({ 'axy' : result.axy() })
    if(_fonctionName == 'ay'):
        return jsonify({ 'ay' : result.ay() })
    if(_fonctionName == 'ax_y'):
        return jsonify({ 'ax_y' : result.ax_y() })
    if(_fonctionName == 'commspouse'):
        return jsonify({
        'ax_y' : result.ax_y(),
    }) 

#commexpense--------------------------------------------------------------------------->
@REQUEST_API.route('/commexpense/<string:_fonctionName>', methods=['GET','POST'])
@oidc.require_login
def commexpense(_fonctionName):
    
    arguments = request.json
    
    result = Commexpense(arguments.get('sex'), float(arguments.get('client_age_last_birthday')), float(arguments.get('Adj_Inf_Disc_Rat')), float(arguments.get('Guar_period')),Male,Female)

    if(_fonctionName == 'table'):
        return jsonify({ 'table' : result.table().to_json(orient='records').replace('"', '') })
    if(_fonctionName == 'ax'):
        return jsonify({ 'ax' : result.ax() })
    if(_fonctionName == 'commexpense'):
        return jsonify({
        'ax' : result.ax(),
    })

#commutation--------------------------------------------------------------------------->
@REQUEST_API.route('/commutation/<string:_fonctionName>', methods=['GET','POST'])
@oidc.require_login
def commutation(_fonctionName):
    
    arguments = request.json
    
    result = Commutation(arguments.get('sex'), float(arguments.get('client_age_last_birthday')), float(arguments.get('Adj_disc_R')), float(arguments.get('Guar_period')),Male,Female)
    
    #Initialisation
    A=Commutation('M',67,0.1125,10,Male,Female)
    A.Male_table()
    A.Female_table()
    A.ax()
    A.gpx()

    if(_fonctionName == 'Male_table'):
        return jsonify({ 'Male_table': result.Male_table().to_json(orient='records').replace('"', '') })
    if(_fonctionName == 'Female_table'):
        return jsonify({ 'Female_table': result.Female_table().to_json(orient='records').replace('"', '') })
    if(_fonctionName == 'ax'):
        return jsonify({ 'ax' : result.ax() })
    if(_fonctionName == 'gpx'):
        return jsonify({ 'gpx' : result.gpx() })
    if(_fonctionName == 'commutation'):
        return jsonify({
        'Male_table': result.Male_table().to_json(orient='records').replace('"', ''),
        'Female_table' : result.Female_table().to_json(orient='records').replace('"', ''),
        'ax' : result.ax(),
        'gpx' : result.gpx(),
    })

#Pricing--------------------------------------------------------------------------->
@REQUEST_API.route('/pricing/<string:_fonctionName>', methods=['GET','POST'])
@oidc.require_login
def pricing(_fonctionName):
    
    arguments = request.json

    result = Pricing(Adj_disc_R = float(arguments.get('Adj_disc_R')),
            Guar_period = float(arguments.get('Guar_period')),
            M_Adj_Disc_R = float(arguments.get('M_Adj_Disc_R')), 
            gpx = float(arguments.get('gpx')), 
            ax_commutation = float(arguments.get('ax_commutation')),
            annuity_freq = float(arguments.get('annuity_freq')),
            Var_Expperannuity = float(arguments.get('Var_Expperannuity')),
            ax_comexp = float(arguments.get('ax_comexp')),
            Rend_fix_exp = float(arguments.get('Rend_fix_exp')),
            Initial_Expense = float(arguments.get('Initial_Expense')),
            Profit_Mar = float(arguments.get('Profit_Mar')),
            comm_Rate = float(arguments.get('comm_Rate')),
            spouse_option = float(arguments.get('spouse_option')),
            ax_h = float(arguments.get('ax_h')),
            Quote_Required1 = arguments.get('Quote_Required1'),
            Quote_Required2 = arguments.get('Quote_Required2'),
            Premium = float(arguments.get('Premium')))

    #Initialisation
    print(result.PV_Liability())
    print(result.Expense_Liability())
    print(result.Expense_Renewal_Liability())
    print(result.PV_Spouse_Annuity())
    print(result.Expenses_during_spouse_annuity())
    print(result.Annuity())

    if(_fonctionName == "PV_Liability"):
        return jsonify({ 'PV_Liability': result.PV_Liability() })
    if(_fonctionName == "Expense_Liability"):
        return jsonify({ 'Expense_Liability' : result.Expense_Liability() })
    if(_fonctionName == "Expense_Renewal_Liability"):
        return jsonify({ 'Expense_Renewal_Liability' : result.Expense_Renewal_Liability() })
    if(_fonctionName == "PV_Spouse_Annuity"):
        return jsonify({ 'PV_Spouse_Annuity' : result.PV_Spouse_Annuity() })
    if(_fonctionName == "Expenses_during_spouse_annuity"):
        return jsonify({ 'Expenses_during_spouse_annuity' : result.Expenses_during_spouse_annuity() })
    if(_fonctionName == "Annuity"):
        return jsonify({ 'Annuity' : result.Annuity() })
    if(_fonctionName == "pricing"):
        return jsonify({
        'PV_Liability': result.PV_Liability(),
        'Expense_Liability' : result.Expense_Liability(),
        'Expense_Renewal_Liability' : result.Expense_Renewal_Liability(),
        'PV_Spouse_Annuity' : result.PV_Spouse_Annuity(),
        'Expenses_during_spouse_annuity' : result.Expenses_during_spouse_annuity(),
        'Annuity' : result.Annuity()
    })
