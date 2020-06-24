%global srcname stringprep

%global p1_utils_ver 1.0.17


Name: erlang-%{srcname}
Version: 1.0.18
Release: 1%{?dist}

License: ASL 2.0 and TCL
Summary: A framework for preparing Unicode strings to help input and comparison
URL: https://github.com/processone/stringprep/
Source0: https://github.com/processone/stringprep/archive/%{version}/%{srcname}-%{version}.tar.gz

Provides:  erlang-p1_stringprep = %{version}-%{release}
Obsoletes: erlang-p1_stringprep < 1.0.3

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: erlang-rebar
BuildRequires: erlang-p1_utils >= %{p1_utils_ver}

Requires: erlang-p1_utils >= %{p1_utils_ver}


%description
Stringprep is a framework for preparing Unicode test strings in order to
increase the likelihood that string input and string comparison work. The
principle are defined in RFC-3454: Preparation of Internationalized Strings.
This library is leverage Erlang native NIF mechanism to provide extremely fast
and efficient processing.


%prep
%autosetup -n stringprep-%{version}


%build
%{rebar_compile}


%install
install -d $RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/priv/lib

install -pm755 priv/lib/* $RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/priv/lib/
%{erlang_install}


%check
%{rebar_eunit}


%files
%license LICENSE.txt LICENSE.TCL LICENSE.ALL
%doc CHANGELOG.md
%doc README.md
%{erlang_appdir}


%changelog
* Mon Feb 17 2020 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.18-1
- Update to 1.0.18 (#1789037).
- https://github.com/processone/stringprep/blob/1.0.18/CHANGELOG.md

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 26 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.17-2
- Bring stringprep back to s390x (#1772971).

* Thu Nov 14 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.17-1
- Update to 1.0.17 (#1742461).
- https://github.com/processone/stringprep/blob/1.0.17/CHANGELOG.md
- Add an exclusion on s390x (#1770256).

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 05 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.16-1
- Update to 1.0.16 (#1713323).
- https://github.com/processone/stringprep/blob/1.0.16/CHANGELOG.md

* Tue Apr 16 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.15-1
- Update to 1.0.15 (#1683159).
- https://github.com/processone/stringprep/blob/1.0.15/CHANGELOG.md

* Thu Feb 21 2019 Peter Lemenkov <lemenkov@gmail.com> - 1.0.14-3
- Rebuild for Erlang 21

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Oct 14 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.14-1
- Update to 1.0.14.
- https://github.com/processone/stringprep/blob/1.0.14/CHANGELOG.md

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 1.0.12-2
- Rebuild with fixed binutils

* Sun Jul 29 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.12-1
- Update to 1.0.12 (#1596222).
- https://github.com/processone/stringprep/blob/1.0.12/CHANGELOG.md

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 27 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.11-1
- Update to 1.0.11 (#1559661).
- https://github.com/processone/stringprep/blob/1.0.11/CHANGELOG.md

* Sun Mar 25 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.10-4
- Re-rebuild against Erlang 20, this time with feeling (and to fix automatically generated
  dependencies).

* Thu Feb 22 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.10-3
- Rebuild for Erlang 20.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild
