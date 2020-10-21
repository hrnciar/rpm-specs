%global realname clique
%global upstream basho


Name:		erlang-%{realname}
Version:	0.3.10
Release:	6%{?dist}
BuildArch:	noarch
Summary:	CLI Framework for Erlang
License:	ASL 2.0
URL:		https://github.com/%{upstream}/%{realname}
VCS:		scm:git:https://github.com/%{upstream}/%{realname}.git
Source0:	https://github.com/%{upstream}/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
Patch1:		erlang-clique-0001-Tear-down-tests-properly.patch
# https://github.com/basho/clique/pull/84
Patch2:		erlang-clique-0002-nowarn-the-export_all-call.patch
Patch3:		erlang-clique-0003-fix_for_otp_21.patch
BuildRequires:	erlang-cuttlefish
BuildRequires:	erlang-mochiweb
BuildRequires:	erlang-rebar


%description
Clique is an opinionated framework for building command line interfaces in
Erlang. It provides users with an interface that gives them enough power to
build complex CLIs, but enough constraint to make them appear consistent.


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
%doc README.md
%{erlang_appdir}/


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 10 2019 Peter Lemenkov <lemenkov@gmail.com> - 0.3.10-4
- Fix FTBFS with Erlang 21

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 06 2018 Peter Lemenkov <lemenkov@gmail.com> - 0.3.10-1
- Ver. 0.3.10

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 13 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.3.9-5
- Convert to a noarch package.
- Rebuild against the noarch cuttlefish.
- Fix a FTBFS against OTP/20.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 23 2017 Peter Lemenkov <lemenkov@gmail.com> - 0.3.9-1
- Ver. 0.3.9

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 15 2016 Peter Lemenkov <lemenkov@gmail.com> - 0.3.8-1
- Ver. 0.3.8

* Wed May  4 2016 Peter Lemenkov <lemenkov@gmail.com> - 0.3.5-2
- Missing BuildRequires added - mochiweb

* Wed Mar 16 2016 Peter Lemenkov <lemenkov@gmail.com> - 0.3.5-1
- Ver. 0.3.5
