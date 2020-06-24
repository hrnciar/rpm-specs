%global srcname iconv

%global p1_utils_ver 1.0.13

Name:       erlang-%{srcname}
Version:    1.0.10
Release:    6%{?dist}

Summary:    Fast encoding conversion library for Erlang / Elixir
License:    ASL 2.0
URL:        https://github.com/processone/iconv/
Source0:    https://github.com/processone/iconv/archive/%{version}/%{srcname}-%{version}.tar.gz

Provides:   erlang-p1_iconv = %{version}-%{release}
Obsoletes:  erlang-p1_iconv <= 1.0.0-2

BuildRequires: gcc
BuildRequires: erlang-p1_utils >= %{p1_utils_ver}
BuildRequires: erlang-rebar

Requires: erlang-p1_utils >= %{p1_utils_ver}


%description
Erlang bindings for libiconv. This is used by ejabberd.


%prep
%autosetup -n iconv-%{version}


%build
%configure --enable-nif
%{rebar_compile}


%check
%{rebar_eunit}


%install
install -d $RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/priv/lib

install -pm755 priv/lib/iconv.so $RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/priv/lib/
%{erlang_install}


%files
%license LICENSE.txt
%doc README.md
%{erlang_appdir}


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 22 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.10-5
- Rebuild for Erlang 22 (#1775733).

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 21 2019 Peter Lemenkov <lemenkov@gmail.com> - 1.0.10-3
- Rebuild for Erlang 21

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Oct 14 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.10-1
- Update to 1.0.10.
- https://github.com/processone/iconv/blob/1.0.10/CHANGELOG.md

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 1.0.8-2
- Rebuild with fixed binutils

* Sun Jul 29 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.8-1
- Update to 1.0.8 (#1596194).
- https://github.com/processone/iconv/blob/1.0.8/CHANGELOG.md

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 27 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.7-1
- Update to 1.0.7 (#1559640).
- https://github.com/processone/iconv/blob/1.0.7/CHANGELOG.md

* Sun Mar 25 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.6-4
- Re-rebuild against Erlang 20, this time with feeling (and with working dependency detection).
- Explicitly depend on the required version of p1_utils.

* Thu Feb 22 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.6-3
- Rebuild for Erlang 20.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild
