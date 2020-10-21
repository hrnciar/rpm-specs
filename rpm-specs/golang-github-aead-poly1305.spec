# Generated by go2rpm
%bcond_without check
# Avoid noarch package built differently on different architectures
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(golang.org/x/sys/cpu\\)$

# https://github.com/aead/poly1305
%global goipath         github.com/aead/poly1305
%global commit          3fee0db0b63511234f7230da50b72414f6258f10

%gometa

%global godevelheader %{expand:
Requires:       golang(golang.org/x/sys/cpu)}

%global common_description %{expand:
Poly1305 is a fast, one-time authentication function created by Daniel J.
Bernstein. It is infeasible for an attacker to generate an authenticator for a
message without the key. However, a key must only be used for a single message.
Authenticating two different messages with the same key allows an attacker to
forge authenticators for other messages with the same key.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.8%{?dist}
Summary:        Poly1305 message authentication code

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(golang.org/x/sys/cpu)

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
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 23 18:09:11 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.5.20180717git3fee0db
- Update to new macros

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.git3fee0db
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 17 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.3.20180717git3fee0db
- Bump to commit 3fee0db0b63511234f7230da50b72414f6258f10

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git969857f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Apr 12 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180517git969857f
- First package for Fedora
