%global srcname ezlib


Name:       erlang-%{srcname}
Version:    1.0.6
Release:    3%{?dist}

License:    ASL 2.0
Summary:    Native zlib driver for Erlang
URL:        https://github.com/processone/ezlib/
Source0:    https://github.com/processone/ezlib/archive/%{version}/%{srcname}-%{version}.tar.gz

Provides:   erlang-p1_zlib = %{version}-%{release}
Obsoletes:  erlang-p1_zlib <= 1.0.1-2

BuildRequires: gcc
BuildRequires: erlang-rebar
BuildRequires: zlib-devel


%description
A native zlib driver for Erlang / Elixir, used by ejabberd.


%prep
%autosetup -n ezlib-%{version}


%build
%configure --enable-nif
# There is a pull request upstream for this -lz https://github.com/processone/ezlib/pull/1
LDFLAGS="$LDFLAGS -lz" %{rebar_compile}


%check
%{rebar_eunit}


%install
install -d $RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/priv/lib

install -pm755 priv/lib/ezlib_drv.so \
    $RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/priv/lib/
%{erlang_install}


%files
%license LICENSE.txt
%doc CHANGELOG.md
%doc README.md
%{erlang_appdir}


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 05 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.6-1
- Update to 1.0.6 (#1713426).
- https://github.com/processone/ezlib/blob/1.0.6/CHANGELOG.md

* Tue Apr 16 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.5-1
- Update to 1.0.5 (#1683183).
- https://github.com/processone/ezlib/blob/1.0.5/CHANGELOG.md

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 29 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.4-1
- Update to 1.0.4 (#1559855).
- https://github.com/processone/ezlib/blob/1.0.4/CHANGELOG.md

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 14 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.0.3-1
- Update to 1.0.3 (#1515231).
- https://github.com/processone/ezlib/blob/1.0.3/CHANGELOG.md
