%global srcname epc

%global _description %{expand:EPC is an RPC stack for Emacs Lisp and Python-EPC is its server side and client
side implementation in Python. Using Python-EPC, you can easily call Emacs Lisp
functions from Python and Python functions from Emacs. For example, you can use
Python GUI module to build widgets for Emacs.}


Name:           python-%{srcname}
Version:        0.0.5
Release:        1%{?dist}
Summary:        EPC (RPC stack for Emacs Lisp) for Python

License:        GPLv3+
URL:            https://python-epc.readthedocs.org/
Source0:        https://github.com/tkf/%{name}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist nose}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist sexpdata}
BuildArch:      noarch

%description
%{_description}


%package -n python3-%{srcname}
Summary:        %{summary}
Requires:       %{py3_dist sexpdata}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{_description}


%prep
%autosetup

# Remove bundled egg-info
rm -rf *.egg-info


%build
%py3_build


%install
%py3_install


%check
pytest


%files -n python3-%{srcname}
%doc README.rst
%license COPYING
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-*.egg-info


%changelog
* Tue Sep 01 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.0.5-1
- Initial RPM release
