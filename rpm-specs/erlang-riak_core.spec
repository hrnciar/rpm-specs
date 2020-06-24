%global realname riak_core
%global upstream basho


Name:		erlang-%{realname}
Version:	2.1.10
Release:	11%{?dist}
BuildArch:	noarch
Summary:	Distributed systems infrastructure used by Riak
License:	ASL 2.0
URL:		https://github.com/%{upstream}/%{realname}
VCS:		scm:git:https://github.com/%{upstream}/%{realname}.git
Source0:	https://github.com/%{upstream}/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
# https://github.com/basho/riak_core/pull/785
Patch1:		erlang-riak_core-0001-Compilation-on-Erlang-18-now-works.-All-occurences-o.patch
# Fedora-specific
Patch2:		erlang-riak_core-0002-Don-t-use-pbkdf2-as-application.patch
# https://github.com/basho/riak_core/pull/639
Patch3:		erlang-riak_core-0003-Use-poolboy-API-for-stopping-poolboy.patch
# Fedora-specific
Patch4:		erlang-riak_core-0004-Revert-Copy-in-mochiglobal-as-riak_core_mochiglobal.patch
# Fedora-specific
Patch5:		erlang-riak_core-0005-Be-more-greedy-while-loading-schemas.patch
Patch6:		erlang-riak_core-0006-Don-t-use-deprecated-functions.patch
Patch7:		erlang-riak_core-0007-Don-t-threat-warnings-as-errors.patch
# will be proposed to upstream
Patch8:		erlang-riak_core-0008-Remove-the-remaining-of-folsom.patch
# Fedora-specific
Patch9:		erlang-riak_core-0009-Load-cuttlefish-schemas-from-noarch-dir-as-well.patch
BuildRequires:	erlang-basho_stats >= 1.0.3
BuildRequires:	erlang-clique
BuildRequires:	erlang-cluster_info
BuildRequires:	erlang-eleveldb
BuildRequires:	erlang-exometer_core
BuildRequires:	erlang-lager >= 1.2.2
BuildRequires:	erlang-meck
BuildRequires:	erlang-mochiweb
BuildRequires:	erlang-poolboy >= 0.8.1
BuildRequires:	erlang-rebar
BuildRequires:	erlang-riak_ensemble
BuildRequires:	erlang-riak_sysmon >= 1.1.3



%description
Distributed systems infrastructure used by Riak.


%prep
%autosetup -p1 -n %{realname}-%{version}


%build
%{erlang_compile}


%install
%{erlang_install}
install -D -p -m 644 priv/riak_core.schema %{buildroot}%{erlang_appdir}/priv/riak_core.schema


%check
%{erlang_test}


%files
%license LICENSE
%doc README.md docs/*
%{erlang_appdir}/


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 12 2019 Peter Lemenkov <lemenkov@gmail.com> - 2.1.10-10
- Rebuilt with fixed Rebar

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 13 2018 Peter Lemenkov <lemenkov@gmail.com> - 2.1.10-7
- Load schema files from noarch directories as well

* Tue Sep 11 2018 Peter Lemenkov <lemenkov@gmail.com> - 2.1.10-6
- Get rid of folsom

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 13 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.1.10-4
- Convert into a noarch package.
- Rebuild against the noarch lager (#1589611).

* Wed Mar 21 2018 Peter Lemenkov <lemenkov@gmail.com> - 2.1.10-3
- Rebuild for Erlang 20 (with proper builddeps)
- Fix FTBFS with Erlang 20

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Aug 13 2017 Peter Lemenkov <lemenkov@gmail.com> - 2.1.10-1
- Ver. 2.1.10

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Apr 22 2016 Peter Lemenkov <lemenkov@gmail.com> - 2.1.5-1
- Ver. 2.1.5

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jul 02 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.3.2-1
- Ver. 1.3.2

* Sun Mar 24 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.3.1-2
- Fix webmachine dep

* Sun Mar 24 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.3.1-1
- Ver. 1.3.1

* Mon Mar 11 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.3.0-1
- Ver. 1.3.0

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-4.p1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Oct 20 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.2.1-3.p1
- Ver. 1.2.1p1

* Fri Oct 19 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.2.1-2
- Rebuild with new lager

* Wed Oct 10 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.2.1-1
- Ver. 1.2.1

* Wed Sep 05 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.2.0-1
- Ver. 1.2.0

* Thu Jul 19 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.1.2-3
- Re-export one handy function

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri May 18 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.1.2-1
- Ver. 1.1.2

* Fri Feb 25 2011 Peter Lemenkov <lemenkov@gmail.com> - 0.14.1-1
- Ver. 0.14.1

* Sat Jan 22 2011 Peter Lemenkov <lemenkov@gmail.com> - 0.14.0-1
- Ver. 0.14.0
- Dropped upstreamed patch

* Fri Nov 12 2010 Peter Lemenkov <lemenkov@gmail.com> - 0.13.0-1
- Initial build

