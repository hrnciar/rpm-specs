%global realname setup
%global upstream uwiger


Name:		erlang-%{realname}
Version:	2.0.2
Release:	6%{?dist}
BuildArch:	noarch
Summary:	Generic setup utility for Erlang-based systems
License:	ASL 2.0
URL:		https://github.com/%{upstream}/%{realname}
VCS:		scm:git:https://github.com/%{upstream}/%{realname}.git
Source0:	https://github.com/%{upstream}/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
Patch1:		erlang-setup-0001-Don-t-escriptize.patch
Patch2:		erlang-setup-0002-Support-expansion-of-setup-modes-for-find_hooks.patch
BuildRequires:	erlang-rebar


%description
While Erlang/OTP comes with many wonderful applications, including the Mnesia
DBMS, there is no standard or convention for installing a system. Erlang/OTP
provides tools for building a boot script, and rules for setting environment
variables, etc., and Mnesia offers an API for creating and modifying the
database schema.

However, with no convention for when these tools and API functions are called -
and by whom - application developers are left having to invent a lot of code
and scripts, not to mention meditate over chapters of Erlang/OTP documentation
in order to figure out how things fit together.

This utility offers a framework for initializing and configuring a system, with
a set of conventions allowing each component to provide callbacks for different
steps in the installation procedure.

The callbacks are defined through OTP application environment variables, which
can easily be overriden at install time.


%prep
%autosetup -p1 -n %{realname}-%{version}


%build
%{erlang_compile}


%install
%{erlang_install}


%check
%{erlang_test}


%files
%doc doc/ examples/ README.md
%{erlang_appdir}/


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 12 2019 Peter Lemenkov <lemenkov@gmail.com> - 2.0.2-4
- Rebuilt with fixed Rebar

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Sep 14 2018 Peter Lemenkov <lemenkov@gmail.com> - 2.0.2-1
- Ver. 2.0.2

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep 18 2017 Peter Lemenkov <lemenkov@gmail.com> - 1.8.4-1
- Ver. 1.8.4

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb  7 2017 Peter Lemenkov <lemenkov@gmail.com> - 1.8.1-1
- Ver. 1.8.1

* Tue Nov 15 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.8.0-1
- Ver. 1.8.0

* Wed Mar 16 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.7-1
- Ver. 1.7
