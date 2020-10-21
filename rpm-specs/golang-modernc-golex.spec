# Generated by go2rpm
%bcond_without check

# https://gitlab.com/cznic/golex
%global goipath         modernc.org/golex
%global forgeurl        https://gitlab.com/cznic/golex
Version:                1.0.0
%global commit          ecf1ffc390f8ff07443e949b1aa78f28e5954ba3
%global distprefix      %{nil}

%gometa

%global common_description %{expand:
A lex/flex like (not fully POSIX lex compatible) utility.}

%global golicenses      LICENSE
%global godocs          examples AUTHORS CONTRIBUTORS README

Name:           %{goname}
Release:        5%{?dist}
Summary:        Lex/flex like utility

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}
# Go 1.15: https://github.com/golang/go/issues/32479
Patch0:         0001-Convert-int-to-string-using-rune.patch

BuildRequires:  golang(modernc.org/lex)
BuildRequires:  golang(modernc.org/lexer)

%description
%{common_description}

%gopkg

%prep
%goprep
%patch0 -p1

%build
%gobuild -o %{gobuilddir}/bin/golex %{goipath}

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
%doc examples AUTHORS CONTRIBUTORS README
%{_bindir}/*

%gopkgfiles

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 12 17:05:29 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.0-1
- Initial package
