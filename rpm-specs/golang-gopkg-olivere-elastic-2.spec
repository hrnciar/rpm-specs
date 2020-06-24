# Generated by go2rpm
# Need Elasticsearch serve
%bcond_with check

# https://github.com/olivere/elastic
%global goipath         gopkg.in/olivere/elastic.v2
%global forgeurl        https://github.com/olivere/elastic
Version:                2.0.61

%gometa

# Remove in F33:
%global godevelheader %{expand:
Obsoletes:      golang-github-olivere-elastic-devel < 2.0.12-0.12
}

%global common_description %{expand:
Package Elastic provides an interface to the Elasticsearch server.}

%global golicenses      LICENSE
%global godocs          CODE_OF_CONDUCT.md CONTRIBUTING.md CONTRIBUTORS\\\
                        ISSUE_TEMPLATE.md README.md

%global gosupfiles      glide.lock glide.yaml

Name:           %{goname}
Release:        4%{?dist}
Summary:        Elasticsearch client for Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.lock

%if %{with check}
# Tests
BuildRequires:  golang(github.com/fortytw2/leaktest)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
cp %{S:1} %{S:2} .

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.61-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.61-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 09 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.61-2
- Add Obsoletes for old name

* Fri May 17 20:40:17 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 2.0.61-1
- Release 2.0.61

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.12-0.11.git3cfe882
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 2.0.12-0.10.git3cfe882
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.12-0.9.git3cfe882
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 08 2018 Jan Chaloupka <jchaloup@redhat.com> - 2.0.12-0.8.git3cfe882
- Upload glide files

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.12-0.7.git3cfe882
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.12-0.6.git3cfe882
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.12-0.5.git3cfe882
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.12-0.4.git3cfe882
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.12-0.3.git3cfe882
- https://fedoraproject.org/wiki/Changes/golang1.7

* Thu Jun 02 2016 jchaloup <jchaloup@redhat.com> - 2.0.12-0.2.git3cfe882
- Enable devel and unit-test subpackages for epel7
  related: #1327781

* Fri Apr 15 2016 jchaloup <jchaloup@redhat.com> - 2.0.12-0.1.git3cfe882
- First package for Fedora
  resolves: #1327781
