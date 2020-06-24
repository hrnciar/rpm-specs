# Generated by go2rpm
%bcond_without check

# https://github.com/microcosm-cc/bluemonday
%global goipath         github.com/microcosm-cc/bluemonday
Version:                1.0.2
%global commit          89802068f71166e95c92040512bf2e11767721ed

%gometa

%global common_description %{expand:
bluemonday is a HTML sanitizer implemented in Go. It is fast and highly
configurable.

bluemonday takes untrusted user generated content as an input, and will
return HTML that has been sanitised against a whitelist of approved HTML
elements and attributes so that you can safely include the content in your
web page.}

%global golicenses      LICENSE.md
%global godocs          CONTRIBUTING.md CREDITS.md README.md

Name:           %{goname}
Release:        4%{?dist}
Summary:        Fast golang HTML sanitizer

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(golang.org/x/net/html)

%description
%{common_description}

%gopkg

%prep
%goprep

%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE.md
%doc CONTRIBUTING.md CREDITS.md README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 01 17:24:16 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.2-2.20190601git8980206
- Bump to commit 89802068f71166e95c92040512bf2e11767721ed

* Mon Mar 11 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.2-1
- Release 1.0.2 (#1687379)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 25 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.1-1
- Update to 1.0.1
- Fix FTBFS

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.gitf0761eb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.2.20180628gitf0761eb
- Bump to commit f0761eb8ed07c1cc892ef631b00c33463b9b6868

* Sat Mar 24 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180418git995366f
- First package for Fedora

