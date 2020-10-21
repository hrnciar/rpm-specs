%global realname lager
%global upstream erlang-lager


Name:       erlang-%{realname}
Version:    3.8.0
Release:    4%{?dist}
BuildArch:  noarch
Summary:    A logging framework for Erlang/OTP
License:    ASL 2.0
URL:        http://github.com/%{upstream}/%{realname}
VCS:        scm:git:https://github.com/%{upstream}/%{realname}.git
Source0:    https://github.com/%{upstream}/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
BuildRequires:  erlang-goldrush >= 0.1.9
BuildRequires:  erlang-rebar


%description
Lager (as in the beer) is a logging framework for Erlang. Its purpose is to
provide a more traditional way to perform logging in an erlang application that
plays nicely with traditional UNIX logging tools like logrotate and syslog.


%prep
%autosetup -n %{realname}-%{version}


%build
%{erlang_compile}


%install
%{erlang_install}


%check
# Sometimes the tests fail on Rawhide:
# https://github.com/erlang-lager/lager/issues/463
%{erlang_test}


%files
%license LICENSE
%doc README.md
%{erlang_appdir}/


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 15 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.8.0-1
- Update to 3.8.0 (#1742664).
- https://github.com/erlang-lager/lager/blob/3.8.0/README.md#3x-changelog

* Mon Nov 11 2019 Peter Lemenkov <lemenkov@gmail.com> - 3.7.0-3
- Rebuild with fixed Rebar

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 05 2019 Peter Lemenkov <lemenkov@gmail.com> - 3.7.0-1
- Update to 3.7.0 (#1713825).

* Fri May 17 2019 Peter Lemenkov <lemenkov@gmail.com> - 3.6.10-1
- Update to 3.6.10 (#1704974).

* Wed Mar 27 2019 Peter Lemenkov <lemenkov@gmail.com> - 3.6.9-1
- Update to 3.6.9 (#1688337).

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 29 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.6.4-1
- Update to 3.6.4 (#1600506).
- https://github.com/erlang-lager/lager/blob/3.6.4/README.md#3x-changelog

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 17 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.6.3-2
- Rebuild against the noarch version of goldrush.

* Sun Jun 17 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.6.3-1
- Update to 3.6.3 (#1588215).
- https://github.com/erlang-lager/lager/blob/3.6.3/README.md#3x-changelog

* Sat May 05 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.6.2-1
- Update to 3.6.2 (#1539945).
- https://github.com/erlang-lager/lager/blob/3.6.2/README.md#3x-changelog

* Sun Mar 25 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.5.2-3
- Convert into a noarch package.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Oct 26 2017 Peter Lemenkov <lemenkov@gmail.com> - 3.5.2-1
- Ver. 3.5.2

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Peter Lemenkov <lemenkov@gmail.com> - 3.5.1-1
- Ver. 3.5.1
- New upstream

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild
