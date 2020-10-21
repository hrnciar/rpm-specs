# Generated by go2rpm 1
%bcond_with check

# https://github.com/HouzuoGuo/tiedot
%global goipath         github.com/HouzuoGuo/tiedot
Version:                3.4
%global tag             3.4
%global commit          6fb216206052eb2ae4306cf5e75acfa88f60d481

%gometa

%global common_description %{expand:
Your NoSQL database powered by Golang.}

%global golicenses      LICENSE LICENSE-gommap
%global godocs          doc README.md README-gommap.md

Name:           tiedot
Release:        3%{?dist}
Summary:        NoSQL database

# Upstream license specification: BSD-3-Clause and BSD-2-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/dgrijalva/jwt-go)
BuildRequires:  golang(github.com/dgrijalva/jwt-go/request)
BuildRequires:  systemd-rpm-macros

Requires:       curl

%description
%{common_description}

%gopkg

%prep
%goprep
mv %{_builddir}/tiedot-%{tag}/gommap/LICENSE LICENSE-gommap
mv %{_builddir}/tiedot-%{tag}/gommap/README.md README-gommap.md

%build
%gobuild -o %{gobuilddir}/bin/tiedot %{goipath}

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_unitdir}
install -p -m 0644 distributable/tiedot.service %{buildroot}%{_unitdir}/tiedot.service

%if %{with check}
%check
%gocheck
%endif

%post
%systemd_post tiedot.service

%preun
%systemd_preun tiedot.service

%postun
%systemd_postun_with_restart tiedot.service

%files
%license LICENSE LICENSE-gommap
%doc doc README.md README-gommap.md
%{_bindir}/*
%{_unitdir}/tiedot.service

%gopkgfiles

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 30 2020 Fabian Affolter <mail@fabian-affolter.ch> - 3.4-2.20200530git6fb2162
- Fix license naming
- Enable tests as upstream removed the unlicensed dependency
- Add systemd unit file (rhbz#1819257)

* Mon Mar 30 2020 Fabian Affolter <mail@fabian-affolter.ch> - 3.4-1.20200330git3246d2a
- Initial package
