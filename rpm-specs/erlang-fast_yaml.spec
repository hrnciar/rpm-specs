%global srcname fast_yaml

%global p1_utils_ver 1.0.17

Name: erlang-%{srcname}
Version: 1.0.22
Release: 1%{?dist}

License: ASL 2.0
Summary: An Erlang wrapper for libyaml "C" library
URL:     https://github.com/processone/fast_yaml/
Source0: https://github.com/processone/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

Provides:  erlang-p1_yaml = %{version}-%{release}
Obsoletes: erlang-p1_yaml < 1.0.2

BuildRequires: gcc
BuildRequires: erlang-rebar
BuildRequires: erlang-p1_utils >= %{p1_utils_ver}
BuildRequires: libyaml-devel

Requires: erlang-p1_utils >= %{p1_utils_ver}


%description
P1 YAML is an Erlang wrapper for libyaml "C" library.


%prep
%autosetup -n %{srcname}-%{version}


%build
%{rebar_compile}


%install
%{erlang_install}

install -d $RPM_BUILD_ROOT%{_libdir}/erlang/lib/%{srcname}-%{version}/priv/lib

install -pm755 priv/lib/* $RPM_BUILD_ROOT%{_libdir}/erlang/lib/%{srcname}-%{version}/priv/lib


%check
%{rebar_eunit}


%files
%license LICENSE.txt
%doc CHANGELOG.md
%doc README.md
%{erlang_appdir}


%changelog
* Mon Feb 17 2020 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.22-1
- Update to 1.0.22 (#1789167).
- https://github.com/processone/fast_yaml/blob/1.0.22/CHANGELOG.md

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 26 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.21-2
- Bring fast_yaml back to s390x (#1772969).

* Thu Nov 14 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.21-1
- Update to 1.0.21 (1742455).
- https://github.com/processone/fast_yaml/blob/1.0.20/CHANGELOG.md
- https://github.com/processone/fast_yaml/blob/1.0.21/CHANGELOG.md
- Add an exclusion on s390x (#1770256).

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 05 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.19-1
- Update to 1.0.19 (#1713301).
- https://github.com/processone/fast_yaml/blob/1.0.19/CHANGELOG.md

* Tue Apr 16 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.18-1
- Update to 1.0.18 (#1683116).
- https://github.com/processone/fast_yaml/blob/1.0.18/CHANGELOG.md

* Thu Feb 21 2019 Peter Lemenkov <lemenkov@gmail.com> - 1.0.17-3
- Rebuild for Erlang 21

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild
