%global realname p1_pgsql
%global upstream processone


Name:       erlang-%{realname}
Version:    1.1.8
Release:    4%{?dist}
BuildArch:  noarch

License:    ERPL
Summary:    Pure Erlang PostgreSQL driver
URL:        https://github.com/%{upstream}/%{realname}
%if 0%{?el7}%{?fedora}
VCS:        scm:git:https://github.com/%{upstream}/%{realname}.git
%endif
Source0:    https://github.com/%{upstream}/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz

Provides:   erlang-pgsql = %{version}-%{release}
Obsoletes:  erlang-pgsql < 0-16

BuildRequires: erlang-rebar


%description
Pure Erlang PostgreSQL driver.


%prep
%autosetup -n %{realname}-%{version}


%build
%{erlang_compile}


%install
%{erlang_install}


%check
%{erlang_test}


%files
%license EPLICENSE
%doc README.md
%{erlang_appdir}/


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 14 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.1.8-3
- Rebuild for https://bugzilla.redhat.com/show_bug.cgi?id=1748545

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 05 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.1.8-1
- Update to 1.1.8 (#1713424).
- https://github.com/processone/p1_pgsql/blob/1.1.8/CHANGELOG.md

* Tue Apr 16 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.1.7-1
- Update to 1.1.7 (#1683181).
- https://github.com/processone/p1_pgsql/blob/1.1.7/CHANGELOG.md

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 29 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.1.6-1
- Update to 1.1.6 (#1596210).
- https://github.com/processone/p1_pgsql/blob/1.1.6/CHANGELOG.md

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 27 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.1.5-1
- Update to 1.1.5 (#1496443).
- https://github.com/processone/p1_pgsql/blob/1.1.5/CHANGELOG.md

* Sun Mar 25 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.1.3-3
- Convert into a noarch package.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild
