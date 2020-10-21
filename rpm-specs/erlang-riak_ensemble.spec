%global realname riak_ensemble
%global upstream basho


Name:		erlang-%{realname}
Version:	2.1.9
Release:	8%{?dist}
Summary:	Multi-Paxos framework in Erlang
License:	ASL 2.0
URL:		https://github.com/%{upstream}/%{realname}
VCS:		scm:git:https://github.com/%{upstream}/%{realname}.git
Source0:	https://github.com/%{upstream}/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
Patch1:		erlang-riak_ensemble-0001-Remove-deprecated-BIF.patch
Patch2:		erlang-riak_ensemble-0002-Fix-deprecation-warning-while-building-with-Erlang-1.patch
Patch3:		erlang-riak_ensemble-0003-Don-t-treat-warns-as-errors.patch
BuildRequires:  gcc
BuildRequires:	erlang-eleveldb
BuildRequires:	erlang-lager
BuildRequires:	erlang-rebar
#BuildRequires:	erlang-riak_test
# Remove when https://bugzilla.redhat.com/show_bug.cgi?id=1770256 is resolved
ExcludeArch: s390x


%description
A consensus library that supports creating multiple consensus groups
(ensembles). Each ensemble is a separate Multi-Paxos instance with its own
leader, set of members, and state.

Each ensemble also supports an extended API that provides consistent key/value
operations. Conceptually, this is identical to treating each key as a separate
Paxos entity. However, this isn't accomplished by having each key maintain its
own Paxos group. Instead, an ensemble emulates per-key consensus through a
combination of per-key and per-ensemble state.


%prep
%autosetup -p1 -n %{realname}-%{version}


%build
%{erlang_compile}


%install
%{erlang_install}


%check
#%%{erlang_test}


%files
%license LICENSE
%doc doc/ README.md
%{erlang_appdir}/


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.9-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 12 2019 Peter Lemenkov <lemenkov@gmail.com> - 2.1.9-5
- Rebuild for Erlang 22

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 21 2019 Peter Lemenkov <lemenkov@gmail.com> - 2.1.9-3
- Rebuild for Erlang 21

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 06 2018 Peter Lemenkov <lemenkov@gmail.com> - 2.1.9-1
- Ver. 2.1.9

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 13 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.1.8-6
- Rebuild against the noarch lager (#1589611).
- BuildRequire gcc.

* Wed Mar 21 2018 Peter Lemenkov <lemenkov@gmail.com> - 2.1.8-5
- Rebuild for Erlang 20 (with proper builddeps)

* Tue Mar 06 2018 Peter Lemenkov <lemenkov@gmail.com> - 2.1.8-4
- Fix FTBFS with Erlang 20

* Fri Feb 23 2018 Peter Lemenkov <lemenkov@gmail.com> - 2.1.8-3
- Rebuild for Erlang 20

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 21 2017 Peter Lemenkov <lemenkov@gmail.com> - 2.1.7-1
- Ver. 2.1.7

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Aug 17 2016 Peter Lemenkov <lemenkov@gmail.com> - 2.1.2-4
- Fix FTBFS with Erlang 19

* Sun Aug 07 2016 Igor Gnatenko <ignatenko@redhat.com> - 2.1.2-3
- Rebuild for Erlang 19

* Thu Jun  2 2016 Peter Lemenkov <lemenkov@gmail.com> - 2.1.2-2
- Re-enable debuginfo generation disabled by mistake

* Wed Mar 16 2016 Peter Lemenkov <lemenkov@gmail.com> - 2.1.2-1
- Ver. 2.1.2
