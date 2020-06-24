# setup.py does not list all requirements, and we also unbundle quite a few
# from the externals folder, so we can't only rely on the automatic generator
# here.
# Additionally, requirements.txt seems to be dev requirements, and is not used
# in setup.py for install_requires.

%global modname mne

Name:           python-%{modname}
Version:        0.20.7
Release:        1%{?dist}
Summary:        Magnetoencephalography (MEG) and Electroencephalography (EEG) data analysis

# Bundled FieldTrip
# https://github.com/fieldtrip/fieldtrip/blob/master/realtime/src/buffer/python/FieldTrip.py
# Not possible to package because it is matlab package with some plugins

License:        BSD
URL:            http://martinos.org/mne/
Source0:        https://github.com/mne-tools/mne-python/archive/v%{version}/%{name}-%{version}.tar.gz
#Source1:        https://s3.amazonaws.com/mne-python/datasets/MNE-sample-data-processed.tar.gz
BuildArch:      noarch

%description
This package is designed for sensor- and source-space analysis of M-EEG data,
including frequency-domain and time-frequency analyses and non-parametric
statistics.

%{?python_enable_dependency_generator}

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
Provides:       bundled(bootstrap)
Provides:       bundled(js-jquery)
Provides:       bundled(js-jquery-ui)
Provides:       bundled(js-d3)
Provides:       bundled(js-mpld3)
Provides:       bundled(python3-FieldTrip)
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-numpy
BuildRequires:  python3-scipy

# Test deps
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-pytest-mock
BuildRequires:  python3-pytest-xdist
BuildRequires:  python3-pytest-timeout
BuildRequires:  python3-matplotlib
BuildRequires:  python3-pandas
BuildRequires:  python3-h5py
BuildRequires:  python3-decorator
BuildRequires:  python3-pymatreader
BuildRequires:  python3-h5io
BuildRequires:  python3-tempita
BuildRequires:  python3-scikit-learn
BuildRequires:  python3-Traits
BuildRequires:  python3-tqdm
BuildRequires:  python3-nibabel
BuildRequires:  python3-nilearn
BuildRequires:  python3-qt5
BuildRequires:  python3-dipy
BuildRequires:  python3-xlrd

Requires:       python3-matplotlib
Requires:       python3-decorator
Requires:       python3-h5io
Requires:       python3-six
Requires:       python3-tempita
Requires:       python3-funcsigs
Requires:       python3-pymatreader
Recommends:     python3-scikit-learn
Recommends:     python3-pandas
Recommends:     python3-patsy
Recommends:     python3-pillow
Recommends:     python3-h5py
Recommends:     python3-statsmodels
Recommends:     python3-Traits

# Should be included by the dep generator as they're mentioned in setup.py
# Requires:       python3-numpy
# Requires:       python3-scipy

%description -n python3-%{modname}
This package is designed for sensor- and source-space analysis of M-EEG data,
including frequency-domain and time-frequency analyses and non-parametric
statistics.

Python 3 version.

%prep
%autosetup -n %{modname}-python-%{version}

pushd %{modname}/externals/
  # Remove bundled six, tqdm, decorator, tempita, h5io
  # Save bundled FieldTrip (can't find upstream)
  rm -rf decorator.py doccer.py pymatreader/ tempita/ h5io/ tqdm/
  # Check that only {FieldTrip,__init__}.py remain
  [ $(find -maxdepth 1 -mindepth 1 | grep -v FieldTrip.py | grep -v __init__.py | wc -l) -eq 0 ] || exit 1
popd
# use all six/tqdm/decorator/h5io/funcsigs/pymatreader from system
# fix API change for jdjcal/jcal2jd
find -type f -name '*.py' -exec sed -i \
  -e "s/from mne.externals.six/from six/" \
  -e "s/from \.*externals.six/from six/" \
  -e "s/from mne.externals import six/import six/" \
  -e "s/from \.*externals import six/import six/" \
  -e "s/from \.*externals.decorator/from decorator/" \
  -e "s/from mne.externals.h5io/from h5io/" \
  -e "s/from \.*externals.h5io/from h5io/" \
  -e "s/from \.*externals.tempita/from tempita/" \
  -e "s/from \.*externals.funcsigs/from funcsigs/" \
  -e "s/from \.*externals.pymatreader/from pymatreader/" \
  -e "s/from mne.externals.pymatreader/from pymatreader/" \
  -e "s/from \.*.externals.tqdm/from tqdm/" \
  -e "s/from mne.externals.tqdm/from tqdm/" \
  -e "s/from \.*externals.doccer/from scipy.misc.doccer/" \
  -e "s/jd2jcal(\(.*\))/jd2jcal(\1, 0)[:-1]/" \
  -e "s/(jcal2jd(\(.*\)))/(jcal2jd(\1)[-1])/" \
  {} ';'
sed -i -e "/mne\.externals\.[^']*/d" setup.py

sed -i -e '1{\@^#!/usr/bin/env python@d}' %{modname}/commands/*.py

#cp -p %{SOURCE1} .
#python -c "import mne; mne.datasets.sample.data_path(verbose=True, download=False)"

%build
%py3_build

%install
%py3_install

%check
export MNE_SKIP_TESTING_DATASET_TESTS=true
export MNE_SKIP_NETWORK_TESTS=1
export MNE_DONTWRITE_HOME=true
export MNE_FORCE_SERIAL=true

export PYTHONPATH=%{buildroot}%{python3_sitearch}

# Deselected tests require additional data or don't work in mock
# Two deselected for sklearn warnings:
pytest-%{python3_version}\
 --deselect mne/utils/tests/test_logging.py\
 --deselect mne/tests/test_report.py\
 --deselect mne/beamformer/tests/test_lcmv.py\
 --deselect mne/io/curry/tests/test_curry.py\
 --deselect mne/io/tests/test_meas_info.py\
 --deselect mne/tests/test_chpi.py\
 --deselect mne/viz/tests/test_topomap.py\
 --deselect mne/preprocessing/tests/test_peak_finder.py\
 --deselect mne/io/tests/test_constants.py\
 --deselect mne/datasets/tests/test_datasets.py


%files -n python3-%{modname}
%license LICENSE.txt
%doc README.rst examples
%{_bindir}/%{modname}
%{python3_sitelib}/%{modname}/
%{python3_sitelib}/%{modname}-*.egg-info/

%changelog
* Sun Jun 21 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.20.7-1
- Update to 0.20.7

* Tue Jun 02 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.20.4-2
- Deselect failing tests: test_scalar, test_get_coef
- https://github.com/mne-tools/mne-python/issues/7860

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.20.4-2
- Rebuilt for Python 3.9

* Sat Apr 04 2020 Aniket Pradhan <major AT fedoraproject DOT org> - 0.20.4-1
- Update to v0.20.4
- Fix dependencies (removed jdcal, added tqdm and others)
- Deselected tests that require additional data

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 11 2019 Aniket Pradhan <major AT fedoraproject DOT org> - 0.19.1-1
- Update to v0.19.1

* Thu Oct 10 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.19.0-1
- Update to new upstream release

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.18.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 28 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.18.1-1
- Update to 0.18.1 (rbhz 1695469)
- Use dep generator
- Remove bundled doccer
- Remove missing AUTHORS file

* Fri Feb 22 2019 Manas Mangaonkar <pac23 AT fedoraproject DOT org> - 0.17.1-1
- Update to latest release

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 20 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.17-1
- Update to latest release
- Use system funcsigs and pymatreader

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.13.1-9
- Subpackage python2-mne has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.13.1-7
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.13.1-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.13.1-2
- Rebuild for Python 3.6

* Tue Nov 29 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.13.1-1
- Update to 0.13.1

* Mon Sep 26 2016 Dominik Mierzejewski <rpm@greysector.net> - 0.10-8
- rebuilt for matplotlib-2.0.0

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-7
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 29 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.10-5
- Rebuild for fixed scipy

* Wed Nov 11 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.10-4
- Fix non-executable-script

* Mon Nov 09 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.10-3
- Fix unbundling jdcal

* Sun Nov 08 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.10-2
- /usr/bin/mne uses python3
- fix dependencies around Traits (add py3 version)
- unbundle jdcal/six/decorator/tempita/h5io
- add Provides: bundled(pythonX-FieldTrip)
- More better Summary

* Fri Oct 30 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.10-1
- Initial package
