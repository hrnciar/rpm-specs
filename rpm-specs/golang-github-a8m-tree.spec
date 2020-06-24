# Generated by go2rpm
%bcond_without check

# https://github.com/a8m/tree
%global goipath         github.com/a8m/tree
%global commit          6a0b80129de45f91880d18428b95fab29df91d7e

%gometa

%global common_description %{expand:
An implementation of the Unix tree command written in Go, that can be used
programmatically.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.7%{?dist}
Summary:        Implementation of the Unix tree command written in Go
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%build
%gobuild -o %{gobuilddir}/bin/gotree %{goipath}/cmd/tree

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 20:01:01 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.5.20190225git6a0b801
- Update to new macros

* Mon Feb 25 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20190225git6a0b801
- Bump to commit 6a0b80129de45f91880d18428b95fab29df91d7e

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.git3cf936c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git3cf936c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 20 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180422gitcf42b1e
- First package for Fedora
