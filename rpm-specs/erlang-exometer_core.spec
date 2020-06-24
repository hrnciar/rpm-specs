%global realname exometer_core
%global upstream feuerlabs


Name:		erlang-%{realname}
Version:	1.5.0
Release:	9%{?dist}
BuildArch:	noarch
Summary:	Easy and efficient instrumentation of Erlang code
License:	MPLv2.0
URL:		https://github.com/%{upstream}/%{realname}
VCS:		scm:git:https://github.com/%{upstream}/%{realname}.git
Source0:	https://github.com/%{upstream}/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
# Fedora/EPEL specific
Patch1:		erlang-exometer-core-0001-Temporary-revert-checking-for-aliases.patch
Patch2:		erlang-exometer-core-0002-Bundle-hut-header.patch
BuildRequires:	erlang-edown
BuildRequires:	erlang-folsom
BuildRequires:	erlang-lager
BuildRequires:	erlang-meck
BuildRequires:	erlang-parse_trans
BuildRequires:	erlang-rebar
BuildRequires:	erlang-setup


%description
The Exometer Core package allows for easy and efficient instrumentation of
Erlang code, allowing crucial data on system performance to be exported to a
wide variety of monitoring systems.

Exometer Core comes with a set of predefined monitor components, and can be
expanded with custom components to handle new types of Metrics, as well as
integration with additional external systems such as databases, load balancers,
etc.


%prep
%autosetup -p1 -n %{realname}-%{version}


%build
%{erlang_compile}


%install
%{erlang_install}


%check
%{erlang_test}


%files
%license LICENSE
%doc doc/ README.md
%{erlang_appdir}/


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 12 2019 Peter Lemenkov <lemenkov@gmail.com> - 1.5.0-8
- Rebuilt with fixed Rebar

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 01 2018 Peter Lemenkov <lemenkov@gmail.com> - 1.5.0-4
- Make it noarch

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 14 2017 Peter Lemenkov <lemenkov@gmail.com> - 1.5.0-1
- Ver. 1.5.0

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.4-2
- Fix tests in riak_kv with patch no.1

* Wed Mar 16 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.4-1
- Ver. 1.4
