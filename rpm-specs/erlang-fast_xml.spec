%global srcname fast_xml

%global p1_utils_ver 1.0.17

Name: erlang-%{srcname}
Version: 1.1.38
Release: 1%{?dist}

License: ASL 2.0
Summary: Fast Expat based Erlang XML parsing and manipulation library
URL:     https://github.com/processone/fast_xml/
Source0: https://github.com/processone/fast_xml/archive/%{version}/%{srcname}-%{version}.tar.gz

Provides:  erlang-p1_xml = %{version}-%{release}
Obsoletes: erlang-p1_xml < 1.1.11

BuildRequires: gcc
BuildRequires: erlang-edoc
BuildRequires: erlang-rebar
BuildRequires: erlang-p1_utils >= %{p1_utils_ver}
BuildRequires: expat-devel

Requires: erlang-p1_utils >= %{p1_utils_ver}


%description
Fast Expat based Erlang XML parsing and manipulation library, with a strong
focus on XML stream parsing from network. It supports full XML structure
parsing, suitable for small but complete XML chunks, and XML stream parsing
suitable for large XML document, or infinite network XML stream like XMPP.
This module can parse files much faster than built-in module xmerl. Depending
on file complexity and size xml_stream:parse_element/1 can be 8-18 times faster
than calling xmerl_scan:string/2.


%prep
%autosetup -n fast_xml-%{version}


%build
%{rebar_compile}


%install
%{erlang_install}

install -p -D -m 755 priv/lib/* --target-directory=$RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/priv/lib/


%check
%{rebar_eunit}


%files
%license LICENSE.txt
%doc CHANGELOG.md README.md
%{erlang_appdir}


%changelog
* Mon Feb 17 2020 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.1.38-1
- Update to 1.1.38 (#1789168).
- https://github.com/processone/fast_xml/blob/1.1.38/CHANGELOG.md

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.37-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 26 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.1.37-2
- Bring fast_xml back to s390x (#1772968).

* Thu Nov 14 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.1.37-1
- Update to 1.1.37 (#1742456).
- https://github.com/processone/fast_xml/blob/1.1.37/CHANGELOG.md
- Add an exclusion on s390x (#1770256).

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 05 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.1.36-1
- Update to 1.1.36 (#1713300).
- https://github.com/processone/fast_xml/blob/1.1.36/CHANGELOG.md

* Tue Apr 16 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.1.35-1
- Update to 1.1.35 (#1683115).
- https://github.com/processone/fast_xml/blob/1.1.35/CHANGELOG.md

* Thu Feb 21 2019 Peter Lemenkov <lemenkov@gmail.com> - 1.1.34-3
- Rebuild for Erlang 21

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild
