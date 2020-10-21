%global pkgname  jupyterkernel
%global upname   JupyterKernel

Name:           gap-pkg-%{pkgname}
Version:        1.3
Release:        4%{?dist}
Summary:        Jupyter kernel written in GAP
BuildArch:      noarch

License:        BSD
URL:            https://gap-packages.github.io/%{upname}/
Source0:        https://github.com/gap-packages/%{upname}/releases/download/v%{version}/%{upname}-%{version}.tar.gz
# Change setup.py so it installs into the buildroot
Patch0:         %{name}-setup.patch

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-crypting
BuildRequires:  gap-pkg-io
BuildRequires:  gap-pkg-json
BuildRequires:  gap-pkg-uuid
BuildRequires:  gap-pkg-zeromqinterface
BuildRequires:  jupyter-notebook
BuildRequires:  python3dist(jupyter-client)

Requires:       gap-pkg-crypting
Requires:       gap-pkg-io
Requires:       gap-pkg-json
Requires:       gap-pkg-uuid
Requires:       gap-pkg-zeromqinterface
Requires:       python-jupyter-filesystem

%description
This package implements the Jupyter protocol in GAP.

%package doc
Summary:        Jupyter kernel for GAP documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -p0 -n %{upname}-%{version}

%build
export LC_ALL=C.UTF-8
gap < makedoc.g

%install
mkdir -p %{buildroot}%{_bindir}
cp -p bin/jupyter-kernel-gap %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_gap_dir}/pkg/%{upname}-%{version}
cp -a demos doc gap tst *.g %{buildroot}%{_gap_dir}/pkg/%{upname}-%{version}
rm -f %{buildroot}%{_gap_dir}/pkg/%{upname}-%{version}/doc/*.{aux,bbl,blg,idx,ilg,ind,log,out,pnr,tex}

python3 setup.py install --prefix=%{buildroot}%{_prefix}

%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{_gap_dir};%{_gap_dir}" < tst/testall.g

%files
%doc README.md
%license COPYRIGHT.md LICENSE
%{_bindir}/jupyter-kernel-gap
%{_datadir}/jupyter/nbextensions/gap-mode/
%{_datadir}/jupyter/kernels/gap-4/
%{_gap_dir}/pkg/%{upname}-%{version}/
%exclude %{_gap_dir}/pkg/%{upname}-%{version}/demos/
%exclude %{_gap_dir}/pkg/%{upname}-%{version}/doc/

%files doc
%docdir %{_gap_dir}/pkg/%{upname}-%{version}/demos/
%docdir %{_gap_dir}/pkg/%{upname}-%{version}/doc/
%{_gap_dir}/pkg/%{upname}-%{version}/demos/
%{_gap_dir}/pkg/%{upname}-%{version}/doc/

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar  9 2019 Jerry James <loganjerry@gmail.com> - 1.3-1
- Initial RPM
