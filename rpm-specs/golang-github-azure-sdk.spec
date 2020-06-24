# Generated by go2rpm
%bcond_without check

# https://github.com/Azure/azure-sdk-for-go
%global goipath         github.com/Azure/azure-sdk-for-go
Version:                38.2.0

%gometa

# Remove in F33:
%global godevelheader %{expand:
Obsoletes:      golang-github-Azure-azure-sdk-for-go-devel < 15.2.0-5
}

%global common_description %{expand:
Azure-sdk-for-go provides Go packages for managing and using Azure services. It
officially supports the last two major releases of Go.}

%global golicenses      LICENSE NOTICE
%global godocs          CHANGELOG.md CONTRIBUTING.md README.md\\\
                        documentation

Name:           %{goname}
Release:        1%{?dist}
Summary:        Microsoft Azure SDK for Go

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/Azure/go-autorest/autorest)
BuildRequires:  golang(github.com/Azure/go-autorest/autorest/adal)
BuildRequires:  golang(github.com/Azure/go-autorest/autorest/azure)
BuildRequires:  golang(github.com/Azure/go-autorest/autorest/azure/auth)
BuildRequires:  golang(github.com/Azure/go-autorest/autorest/date)
BuildRequires:  golang(github.com/Azure/go-autorest/autorest/to)
BuildRequires:  golang(github.com/Azure/go-autorest/autorest/validation)
BuildRequires:  golang(github.com/Azure/go-autorest/tracing)
BuildRequires:  golang(github.com/globalsign/mgo)
BuildRequires:  golang(github.com/Masterminds/semver)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(github.com/satori/go.uuid)
BuildRequires:  golang(github.com/shopspring/decimal)
BuildRequires:  golang(github.com/spf13/cobra)
BuildRequires:  golang(golang.org/x/crypto/pkcs12)
BuildRequires:  golang(golang.org/x/tools/imports)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/dnaeon/go-vcr/cassette)
BuildRequires:  golang(github.com/dnaeon/go-vcr/recorder)
BuildRequires:  golang(gopkg.in/check.v1)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck -d tools/versioner/cmd
%endif

%gopkgfiles

%changelog
* Tue Jan 28 23:29:12 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 38.2.0-1
- Update to 38.2.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 28.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 28.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 05 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 28.0.0-2
- Add Obsoletes for old name

* Mon Apr 29 18:35:40 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 28.0.0-1
- Release 28.0.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 15.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 15.2.0-3
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 15.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 26 2018 Robert-André Mauchin <zebob.m@gmail.com> - 15.2.0-1
- Upstream release v15.2.0

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 1.2-0.10.20150612git97d9593
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.9.git97d9593
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.8.git97d9593
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.7.git97d9593
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.6.git97d9593
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Aug 09 2016 jchaloup <jchaloup@redhat.com> - 1.2-0.5.git97d9593
- Enable devel and unit-test for epel7
  resolves: #1365467

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-0.4.git97d9593
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-0.3.git97d9593
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.2.git97d9593
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Sep 14 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.git97d9593
- First package for Fedora
  resolves: #1262716
