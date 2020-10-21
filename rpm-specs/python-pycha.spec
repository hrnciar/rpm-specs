%global srcname pycha
%global sum A library for drawing charts with Python and Cairo

Name:           python-%{srcname}
Version:        0.7.0
Release:        18%{?dist}
Summary:        %{sum}

License:        LGPLv3+
URL:            https://bitbucket.org/lgs/pycha/
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
Source1:        chavier.desktop

BuildArch:      noarch
BuildRequires:  desktop-file-utils
BuildRequires:  python3-devel

%description
Pycha is a very simple Python package for drawing charts using the great Cairo
library. Its goals are:
    * Lightweight
    * Simple to use
    * Nice looking with default values
    * Customization 
It won't try to draw any possible chart on earth but draw the most common ones
nicely.

%package -n python3-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3dist(pycairo)
Requires:       python%{python3_version}dist(pycairo)

%description -n python3-%{srcname}
Pycha is a very simple Python package for drawing charts using the great Cairo
library. Its goals are:
    * Lightweight
    * Simple to use
    * Nice looking with default values
    * Customization 
It won't try to draw any possible chart on earth but draw the most common ones
nicely.

%package -n     chavier
Summary:        GUI application for exploring the pycha library
Requires:       python3-%{srcname} = %{version}-%{release}

%description -n chavier
Chavier allows the user to generate random data sets or use existing data to
test the various options that %{shortname} provides in an interactive GUI
application. Various chart types can be plotted and their options adjusted
from the interface.

%prep
%setup -q -n %{srcname}-%{version}

# remove upstream egg-info
rm -rf *.egg-info


%build
2to3 --no-diffs -w chavier pycha tests

# for i in range(len(flat_y) / n_stores)
# TypeError: 'float' object cannot be interpreted as an integer
sed -i 's@ / n_stores@ // n_stores@g' pycha/stackedbar.py

%py3_build


%install
%py3_install

desktop-file-install \
--dir=%{buildroot}%{_datadir}/applications %{SOURCE1}


%check
%{__python3} setup.py test


%files -n python3-%{srcname}
%doc examples/ AUTHORS README.txt
%license COPYING
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-*.egg-info

%files -n chavier
%{_bindir}/chavier
%{_datadir}/applications/chavier.desktop
%{python3_sitelib}/chavier


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7.0-17
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.0-15
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.0-14
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 28 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.0-11
- Fixup Requires

* Thu Dec 27 2018 Miro Hrončok <mhroncok@redhat.com> - 0.7.0-10
- Subpackage python2-pycha has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.7.0-8
- Rebuilt for Python 3.7

* Tue Feb 27 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.7.0-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.7.0-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Jul 15 2016 Dan Horák <dan[at]danny.cz> - 0.7.0-1
- new upstream release 0.7.0
- introduced py3 variant

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 16 2011 Ionuț C. Arțăriși <mapleoin@fedoraproject.org> - 0.6.0-1
- new upstream release 0.6.0

* Sat Aug  7 2010 Ionuț C. Arțăriși <mapleoin@fedoraproject.org> - 0.5.3-1
- new upstream bugfix release

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sat Mar 27 2010 Ionuț C. Arțăriși <mapleoin@fedoraproject.org> - 0.5.2-2
- changed license from LGPLv3 to LGPLv3+
- fixed spelling error in %%description
- capitalized chavier package %%summary
- added pycairo Requires
- removed tests

* Tue Mar 23 2010 Ionuț C. Arțăriși <mapleoin@fedoraproject.org> - 0.5.2-1
- first Fedora release
