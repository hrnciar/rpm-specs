%global modname pyriemann

Name:           python-%{modname}
Version:        0.2.6
Release:        2%{?dist}
Summary:        Covariance matrices manipulation and Biosignal classification

License:        BSD
URL:            https://github.com/alexandrebarachant/pyRiemann
Source0:        %{url}/archive/v%{version}/%{modname}-%{version}.tar.gz

BuildArch:      noarch

%description
pyriemann is a python package for covariance matrices manipulation and
classification through riemannian geometry.

The primary target is classification of multivariate biosignals,
like EEG, MEG or EMG.

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-nose
BuildRequires:  python3-scikit-learn
BuildRequires:  python3-joblib
BuildRequires:  python3-numpy
BuildRequires:  python3-scipy
BuildRequires:  python3-pandas
BuildRequires:  python3-matplotlib
BuildRequires:  python3-seaborn
Requires:       python3-scikit-learn
Requires:       python3-joblib
Requires:       python3-numpy
Requires:       python3-scipy
Requires:       python3-pandas
Requires:       python3-matplotlib

%description -n python3-%{modname}
pyriemann is a python package for covariance matrices manipulation and
classification through riemannian geometry.

The primary target is classification of multivariate biosignals,
like EEG, MEG or EMG.

Python 3 version.

%prep
%autosetup -n pyRiemann-%{version}

%build
%py3_build

%install
%py3_install

%check
pushd tests
  PYTHONPATH=%{buildroot}%{python3_sitelib} nosetests-%{python3_version} -v
popd

%files -n python3-%{modname}
%license LICENSE
%doc README.md examples
%{python3_sitelib}/%{modname}*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.6-2
- Rebuilt for Python 3.9

* Tue Apr 21 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.2.6-1
- Update to 0.2.6

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.4-9
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.2.4-6
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2.4-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Mar 11 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.2.4-1
- Update to 0.2.4

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.2.3-7
- Rebuild for Python 3.6

* Mon Sep 26 2016 Dominik Mierzejewski <rpm@greysector.net> - 0.2.3-6
- rebuilt for matplotlib-2.0.0

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 29 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.2.3-3
- Fix building with new scikit-learn
- Fix requirements a bit

* Thu Nov 12 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.2.3-2
- Fix pandas requirements on f23

* Wed Nov 11 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.2.3-1
- Initial package
