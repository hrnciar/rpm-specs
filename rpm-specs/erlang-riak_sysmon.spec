%global realname riak_sysmon
%global upstream basho


Name:		erlang-%{realname}
Version:	2.1.5
Release:	10%{?dist}
BuildArch:	noarch
Summary:	Rate-limiting system_monitor event handler for Riak
License:	ASL 2.0
URL:		https://github.com/%{upstream}/%{realname}
VCS:		scm:git:https://github.com/%{upstream}/%{realname}.git
Source0:	https://github.com/%{upstream}/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
Patch1:		erlang-riak_sysmon-0001-Move-test-handled-to-test-directory.patch
Patch2:		erlang-riak_sysmon-0002-Remove-example-handler.patch
BuildRequires:	erlang-cuttlefish
BuildRequires:	erlang-rebar


%description
Simple OTP app for managing Erlang VM system_monitor event messages.


%prep
%autosetup -p1 -n %{realname}-%{version}


%build
%{erlang_compile}


%install
%{erlang_install}

cp -arv priv/ %{buildroot}%{erlang_appdir}/


%check
%{erlang_test}


%files
%license LICENSE
%doc doc/ example/ README.md
%{erlang_appdir}/


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 12 2019 Peter Lemenkov <lemenkov@gmail.com> - 2.1.5-9
- Rebuilt with fixed Rebar

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Sep 19 2018 Peter Lemenkov <lemenkov@gmail.com> - 2.1.5-6
- Make it noarch

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 30 2017 Peter Lemenkov <lemenkov@gmail.com> - 2.1.5-1
- Ver. 2.1.5

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Apr 29 2016 Peter Lemenkov <lemenkov@gmail.com> - 2.1.2-1
- Ver. 2.1.2

* Wed Mar 16 2016 Peter Lemenkov <lemenkov@gmail.com> - 2.1.1-1
- Ver. 2.1.1

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 11 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.1.3-2
- Fix file layout

* Mon Mar 11 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.1.3-1
- Ver. 1.1.3

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 07 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.1.2-3
- Stop epmd gracefully after running tests

* Tue May 22 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.1.2-2
- Fixed tests

* Tue May 15 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.1.2-1
- Ver. 1.1.2

* Fri Sep 16 2011 Peter Lemenkov <lemenkov@gmail.com> - 1.0.0-1
- Ver. 1.0.0
