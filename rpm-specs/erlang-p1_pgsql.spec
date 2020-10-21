%global realname p1_pgsql
%global upstream processone


Name:       erlang-%{realname}
Version:    1.1.10
Release:    1%{?dist}
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
* Fri Jul 31 2020 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.1.10-1
- Update to 1.1.10 (#1807013).
- https://github.com/processone/p1_pgsql/blob/1.1.10/CHANGELOG.md

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

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
