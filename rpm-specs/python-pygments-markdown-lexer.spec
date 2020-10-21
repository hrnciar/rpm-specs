
%{!?_licensedir: %global license %%doc}

%global modname pygments-markdown-lexer
%global sum     A Markdown lexer for Pygments to highlight Markdown code snippets

Name:               python-pygments-markdown-lexer
Version:            0.1.0.dev39
Release:            19%{?dist}
Summary:            %{sum}

# One file is BSD, the rest are ASL
# https://fedoraproject.org/wiki/Packaging:LicensingGuidelines#Multiple_Licensing_Scenarios
License:            ASL 2.0 and BSD
URL:                http://pypi.python.org/pypi/pygments-markdown-lexer
Source0:            https://pypi.python.org/packages/source/p/%{modname}/%{modname}-%{version}.zip
BuildArch:          noarch

BuildRequires:      python3-devel
BuildRequires:      python3-setuptools
BuildRequires:      python3-pygments

%description
%{sum}

%package -n python3-%{modname}
Summary:            %{sum}
%{?python_provide:%python_provide python3-%{modname}}

Requires:           python3-pygments

%description -n python3-%{modname}
%{sum}

%prep
%autosetup -n %{modname}-%{version}

%build
%py3_build

%install
%py3_install

# Well this is weird...
rm -rf %{buildroot}/usr/EGG-INFO

%files -n python3-%{modname}
%doc README.md
%license LICENSE
%{python3_sitelib}/pygments_markdown_lexer/
%{python3_sitelib}/pygments_markdown_lexer-%{version}-*

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0.dev39-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.0.dev39-18
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0.dev39-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.0.dev39-16
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.0.dev39-15
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0.dev39-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0.dev39-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 09 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.0.dev39-12
- Subpackage python2-pygments-markdown-lexer has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0.dev39-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.0.dev39-10
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0.dev39-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 27 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.1.0.dev39-8
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0.dev39-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0.dev39-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.1.0.dev39-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0.dev39-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Mar 28 2016 Ralph Bean <rbean@redhat.com> - 0.1.0.dev39-3
- Update setuptools dep for el7.

* Tue Mar 22 2016 Ralph Bean <rbean@redhat.com> - 0.1.0.dev39-2
- Update licensing info as per review.
- Drop el6 macros.

* Thu Mar 17 2016 Ralph Bean <rbean@redhat.com> - 0.1.0.dev39-1
- Initial package for Fedora
