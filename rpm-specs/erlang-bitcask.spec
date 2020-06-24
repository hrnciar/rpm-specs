%global realname bitcask
%global upstream basho


Name:		erlang-%{realname}
Version:	2.0.8
Release:	11%{?dist}
Summary:	Eric Brewer-inspired key/value store
License:	ASL 2.0
URL:		https://github.com/%{upstream}/%{realname}
VCS:		scm:git:https://github.com/%{upstream}/%{realname}.git
Source0:	https://github.com/%{upstream}/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
Source1:	bitcask.licensing
Patch1:		erlang-bitcask-0001-Don-t-use-deprecated-erlang-now-0.patch
Patch2:		erlang-bitcask-0002-Drop-unneeded-eunit-include.patch
Patch3:		erlang-bitcask-0003-Fix-deprecation-warning-while-building-with-Erlang-1.patch
Patch4:		erlang-bitcask-0004-Dont-treat-warnings-as-errors.patch
Patch5:		erlang-bitcask-0005-Support-for-OTP-21.patch
BuildRequires:	erlang-cuttlefish
BuildRequires:	erlang-meck
BuildRequires:	erlang-rebar
BuildRequires:	gcc
# Remove when https://bugzilla.redhat.com/show_bug.cgi?id=1770256 is resolved
ExcludeArch: s390x


%description
Eric Brewer-inspired key/value store.


%prep
%autosetup -p1 -n %{realname}-%{version}


%build
%{erlang_compile}


%install
%{erlang_install}

cp -arv priv/bitcask.schema %{buildroot}%{erlang_appdir}/priv
cp -arv priv/bitcask_multi.schema %{buildroot}%{erlang_appdir}/priv


%check
%{erlang_test}


%files
%doc README.md THANKS doc/
%{erlang_appdir}/


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 12 2019 Peter Lemenkov <lemenkov@gmail.com> - 2.0.8-10
- Rebuild for Erlang 22

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 21 2018 Peter Lemenkov <lemenkov@gmail.com> - 2.0.8-6
- Rebuild for Erlang 20 (with proper builddeps)

* Fri Feb 23 2018 Peter Lemenkov <lemenkov@gmail.com> - 2.0.8-5
- Rebuild for Erlang 20

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar  8 2017 Peter Lemenkov <lemenkov@gmail.com> - 2.0.8-1
- Ver. 2.0.8

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 Peter Lemenkov <lemenkov@gmail.com> - 2.0.7-1
- Ver. 2.0.7

* Thu Oct 20 2016 Peter Lemenkov <lemenkov@gmail.com> - 2.0.6-1
- Ver. 2.0.6

* Tue Aug 16 2016 Peter Lemenkov <lemenkov@gmail.com> - 2.0.3-1
- Ver. 2.0.3
- Fixed FTBFS with Erlang 19

* Sun Aug 07 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.7.4-3
- Rebuild for Erlang 19

* Sun May  8 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.7.4-2
- Remove bogus runtime dependency - eunit

* Sun Apr 17 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.7.4-1
- Ver. 1.7.4

* Fri Apr 15 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.6.1-11
- Drop unneeded macro

* Sat Apr  2 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.6.3-10
- Rebuild with Erlang 18.3

* Fri Feb 12 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.6.3-9
- Fixed FTBFS in Rawhide

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Nov 04 2014 Peter Lemenkov <lemenkov@gmail.com> - 1.6.3-6
- Rebuild with Erlang 17.3.3

* Thu Aug 28 2014 Peter Lemenkov <lemenkov@gmail.com> - 1.6.3-5
- Rebuild with Erlang 17.2.1

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jul 12 2014 Ville Skyttä <ville.skytta@iki.fi> - 1.6.3-3
- Use new erlang macros to build with $RPM_OPT/LD_FLAGS etc, verbosely

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jul 31 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.6.3-1
- Ver. 1.6.3

* Sun Apr 07 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.6.1-1
- Ver. 1.6.1

* Sun Mar 10 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.6.0-1
- Ver. 1.6.0
- Fix FTBFS in Rawhide (F19)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Oct 11 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.5.2-1
- Ver. 1.5.2 (Bugfix release)

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 09 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.5.1-2
- Require specific %%{_isa} to avoid multiarch issues

* Thu May 17 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.5.1-1
- Ver. 1.5.1

* Fri Sep 16 2011 Peter Lemenkov <lemenkov@gmail.com> - 1.2.0-1
- Ver. 1.2.0

* Fri Jan 14 2011 Peter Lemenkov <lemenkov@gmail.com> - 1.1.5-1
- Ver. 1.1.5
- Pass optflags to C-compiler

* Fri Nov 12 2010 Peter Lemenkov <lemenkov@gmail.com> - 1.1.4-1
- Initial build

