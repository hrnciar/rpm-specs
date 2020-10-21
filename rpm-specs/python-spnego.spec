%global pypi_name pyspnego
%global pkg_name spnego

Name:           python-%{pkg_name}
Version:        0.1.1
Release:        2%{?dist}
Summary:        Windows Negotiate Authentication Client and Server

License:        MIT
URL:            https://github.com/jborean93/pyspnego
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Python SPNEGO Library to handle SPNEGO (Negotiate, NTLM, Kerberos)
authentication. Also includes a packet parser that can be used to
decode raw NTLM/SPNEGO/Kerberos tokens into a human readable format.

%package -n     python3-%{pkg_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(cryptography)
%{?python_provide:%python_provide python3-%{pkg_name}}

%description -n python3-%{pkg_name}
Python SPNEGO Library to handle SPNEGO (Negotiate, NTLM, Kerberos)
authentication. Also includes a packet parser that can be used to
decode raw NTLM/SPNEGO/Kerberos tokens into a human readable format.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
# Propably issues with with Python 3.9
%pytest -v tests \
  -k "not test_negotiate_through_python_ntlm \
  and not test_negotiate_with_raw_ntlm \
  and not test_ntlm_auth \
  and not test_sspi_ntlm_auth_no_sign_or_seal \
  and not test_gss_sasl_description_fail \
  and not test_token_rejected \
  and not test_token_no_common_mechs \
  and not test_token_acceptor_first \
  and not test_ntlm_bad_bindings \
  and not test_ntlm_bad_mic \
  and not test_ntlm_no_key_exch \
  and not test_ntlm_lm_request \
  and not test_ntlm_no_lm_allowed \
  and not test_ntlm_nt_v1_request \
  and not test_ntlm_no_nt_v1_allowed \
  and not test_ntlm_invalid_password \
  and not test_ntlm_verify_fail \
  and not test_ntlm_anon_response"

%files -n python3-%{pkg_name}
%license LICENSE
%doc README.md
%{_bindir}/pyspnego-parse
%{python3_sitelib}/spnego/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Sat Sep 12 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.1-2
- Add missing BR (rhbz#1876588)

* Mon Sep 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.1-1
- Initial package for Fedora