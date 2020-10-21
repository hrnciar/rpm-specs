# Generated by go2rpm
# https://github.com/Shopify/logrus-bugsnag/issues/12
%bcond_with check

# https://github.com/Shopify/logrus-bugsnag
%global goipath         github.com/Shopify/logrus-bugsnag
%global commit          577dee27f20dd8f1a529f82210094af593be12bd

%gometa

%global common_description %{expand:
Logrus-bugsnag is a hook that allows Logrus to interface with Bugsnag.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.4%{?dist}
Summary:        Hook that interfaces logrus with bugsnag

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
# https://github.com/Shopify/logrus-bugsnag/issues/11
Patch0:         0001-Replace-Error-with-Errorf.patch

BuildRequires:  golang(github.com/bugsnag/bugsnag-go)
BuildRequires:  golang(github.com/bugsnag/bugsnag-go/errors)
BuildRequires:  golang(github.com/sirupsen/logrus)

%description
%{common_description}

%gopkg

%prep
%goprep
%patch0 -p1

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 02 00:16:32 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190626git577dee2
- Initial package
