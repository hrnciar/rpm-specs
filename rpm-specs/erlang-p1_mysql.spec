%global srcname p1_mysql


Name:       erlang-%{srcname}
Version:    1.0.16
Release:    1%{?dist}
BuildArch:  noarch

Summary:    Pure Erlang MySQL driver
License:    BSD
URL:        https://github.com/processone/p1_mysql/
Source0:    https://github.com/processone/p1_mysql/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires: erlang-eunit
BuildRequires: erlang-rebar
BuildRequires: erlang-rpm-macros


%description
This is an Erlang MySQL driver, used by ejabberd.


%prep
%autosetup -n p1_mysql-%{version}


%build
%{rebar_compile}


%check
%{rebar_eunit}


%install
%{erlang_install}


%files
%license COPYING
%doc README.md
%{_erllibdir}/%{srcname}-%{version}


%changelog
* Fri Jul 31 2020 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.16-1
- Update to 1.0.16 (#1807012).
- https://github.com/processone/p1_mysql/blob/1.0.16/CHANGELOG.md

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Feb 14 2020 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.12-1
- Update to 1.0.12 (#1788908).
- https://github.com/processone/p1_mysql/blob/1.0.12/CHANGELOG.md

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 14 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.11-3
- Rebuild for https://bugzilla.redhat.com/show_bug.cgi?id=1748545

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 16 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.11-1
- Update to 1.0.11 (#1683179).
- https://github.com/processone/p1_mysql/blob/1.0.11/CHANGELOG.md

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 08 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.8-1
- Update to 1.0.8.
- https://github.com/processone/p1_mysql/blob/1.0.8/CHANGELOG.md
