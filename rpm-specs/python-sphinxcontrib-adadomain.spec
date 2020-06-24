%global upstream_name sphinxcontrib-adadomain

Name:           python-%{upstream_name}
Version:        0.2
Release:        12%{?dist}
%global common_summary \
Summary:        Ada domain for the Sphinx documentation generator \
Summary(sv):    Adadomänen för dokumentationsgeneratorn Sphinx
%{common_summary}

License:        BSD
URL:            https://bitbucket.org/tkoskine/sphinxcontrib-adadomain
Source:         https://files.pythonhosted.org/packages/source/s/sphinxcontrib-adadomain/sphinxcontrib-adadomain-%{version}.tar.gz
Patch1:         sphinxcontrib-adadomain-0.2-Directive.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%global common_description_en \
The Ada domain for the Sphinx documentation generator adds support for \
documenting Ada APIs.

%global common_description_sv \
Adadomänen för dokumentationsgeneratorn Sphinx tillför möjligheten att \
dokumentera adagränssnitt.

%description %{common_description_en}

%description -l sv %{common_description_sv}


%package -n python3-%{upstream_name}
%{common_summary}
Requires:       python3-sphinx >= 1.0

%description -n python3-%{upstream_name} %{common_description_en}

%description -n python3-%{upstream_name} -l sv %{common_description_sv}


%prep
%autosetup -n %{upstream_name}-%{version} -p0
rm -rf *.egg-info


%build
%{__python3} setup.py build


%install
%{__python3} setup.py install --skip-build --root %{buildroot}


%files -n python3-%{upstream_name}
%doc README.rst AUTHORS
%license LICENSE
%{python3_sitelib}/*


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2-12
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2-10
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2-9
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 12 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.2-6
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Björn Persson <Bjorn@Rombobjörn.se> - 0.2-5
- Patched to work with Sphinx 1.7.5.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 21 2018 Björn Persson <Bjorn@Rombobjörn.se> - 0.2-1
- Upgraded to 0.2.

* Wed Aug 09 2017 Björn Persson <Bjorn@Rombobjörn.se> - 0.1-11
- Added a Python 3 port.

* Sat Jul 29 2017 Björn Persson <Bjorn@Rombobjörn.se> - 0.1-10
- Changed unversioned "python-" prefixes to "python2-".

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Mar 15 2015 Björn Persson <bjorn@rombobjörn.se> - 0.1-5
- Tagged the license file as such.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Nov 30 2013 Björn Persson <bjorn@rombobjörn.se> - 0.1-3
- Adjusted the description.

* Wed Nov 20 2013 Björn Persson <bjorn@rombobjörn.se> - 0.1-2
- Changed python_sitelib to python2_sitelib.

* Tue Nov 19 2013 Björn Persson <bjorn@rombobjörn.se> - 0.1-1
- ready to be submitted for review
