# Generated by go2rpm
%bcond_without check

# https://github.com/stretchr/objx
%global goipath         honnef.co/go/js/dom
%global forgeurl        https://github.com/dominikh/go-js-dom
%global commit          d6d651dc5aea78554f264a8d6fdc5e994abb2649

%gometa

%global common_description %{expand:
GopherJS bindings for the JavaScript DOM APIs.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.6%{?dist}
Summary:        GopherJS bindings for the JavaScript DOM APIs

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(github.com/gopherjs/gopherjs/js)

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
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 01 18:47:02 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20190601gitd6d651d
- Bump to commit d6d651dc5aea78554f264a8d6fdc5e994abb2649

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.git6da835b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git6da835b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 24 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180420git6da835b
- First package for Fedora
