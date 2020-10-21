# Generated by go2rpm
%bcond_without check

# https://github.com/alexcesaro/quotedprintable
%global goipath         gopkg.in/alexcesaro/quotedprintable.v3
%global forgeurl        https://github.com/alexcesaro/quotedprintable
Version:                3.0.0
%global commit          2caba252f4dc53eaf6b553000885530023f54623

%gometa

# Remove in F33:
%global godevelheader %{expand:
Obsoletes:      golang-gopkg-3-alexcesaro-quotedprintable-devel < 3.0.0-2
}

%global goaltipaths     github.com/alexcesaro/quotedprintable

# Remove in F33:
%global goaltheader %{expand:
Obsoletes:      golang-github-alexcesaro-quotedprintable-v3-devel < 3.0.0-2
}

%global common_description %{expand:
Package Quotedprintable implements quoted-printable and message header encoding
as specified by RFC 2045 and RFC 2047.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        6%{?dist}
Summary:        Go package concerning quoted-printable encoding

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 09 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.0.0-3.20190603git2caba25
- Add Obsoletes for old names

* Mon Jun 03 23:34:48 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 3.0.0-2.20190603git2caba25
- Update to new macros

* Fri Mar 22 2019 Mark Goodwin <mgoodwin@redhat.com> - 3.0.0-1
- First package for Fedora
