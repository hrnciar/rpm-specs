%global srcname     klusta
%global sum     Spike detection and automatic clustering for spike sorting

Name:       python-%{srcname}
Version:    3.0.16
Release:    13%{?dist}
Summary:    %{sum}

License:    BSD
URL:        https://github.com/kwikteam/klusta
Source0:    https://files.pythonhosted.org/packages/source/k/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
klusta is an open source package for automatic spike sorting of multielectrode
neurophysiological recordings made with probes containing up to a few dozens of
sites.

klusta implements the following features:

- Kwik: An HDF5-based file format that stores the results of a spike sorting
  session.
- Spike detection (also known as SpikeDetekt): an algorithm designed for probes
  containing tens of channels, based on a flood-fill algorithm in the adjacency
graph formed by the recording sites in the probe.
- Automatic clustering (also known as Masked KlustaKwik): an automatic
  clustering algorithm designed for high-dimensional structured datasets.

%package -n python3-%{srcname}
Summary:        %{sum}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist numpy six pytest h5py scipy tqdm responses click mock}
Requires:       %{py3_dist numpy scipy six h5py tqdm click}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
klusta is an open source package for automatic spike sorting of multielectrode
neurophysiological recordings made with probes containing up to a few dozens of
sites.

klusta implements the following features:

- Kwik: An HDF5-based file format that stores the results of a spike sorting
  session.
- Spike detection (also known as SpikeDetekt): an algorithm designed for probes
  containing tens of channels, based on a flood-fill algorithm in the adjacency
graph formed by the recording sites in the probe.
- Automatic clustering (also known as Masked KlustaKwik): an automatic
  clustering algorithm designed for high-dimensional structured datasets.


%prep
%autosetup -n %{srcname}-%{version}
rm -fr *egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{srcname}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{srcname}/
%{_bindir}/%{srcname}

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.0.16-13
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.16-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0.16-11
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0.16-10
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.16-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.16-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 31 2018 Miro Hrončok <mhroncok@redhat.com> - 3.0.16-7
- Subpackage python2-klusta has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 3.0.16-5
- Fix build

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.0.16-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 09 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 3.0.16-2
- Update based on review comments 1532082
- use py_dist macros

* Sun Jan 07 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 3.0.16-1
- Initial build
