%global pkg jedi

Name:           emacs-%{pkg}
Version:        0.2.8
Release:        1%{?dist}
Summary:        Python auto-completion for Emacs

License:        GPLv3+
URL:            https://tkf.github.io/%{name}/
Source0:        https://github.com/tkf/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{pkg}-init.el
# Remove useless dependency on argparse module (in Python standard library)
Patch0:         %{name}-0.2.8-python_requires.patch
# Invoke system jediepcserver
Patch1:         %{name}-0.2.8-jediepcserver.patch

BuildRequires:  emacs
BuildRequires:  emacs-auto-complete
BuildRequires:  emacs-epc
BuildRequires:  emacs-python-environment
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}
Requires:       emacs(bin) >= %{_emacs_version}
Requires:       emacs-auto-complete
Requires:       emacs-epc
Requires:       emacs-python-environment
Requires:       jediepcserver
BuildArch:      noarch

%description
Jedi.el is a Python auto-completion package for Emacs. It aims at helping your
Python coding in a non-destructive way. It also helps you to find information
about Python objects, such as docstring, function arguments and code location.


%package -n python3-jediepcserver
Summary:        Jedi EPC server
Provides:       jediepcserver = %{version}-%{release}
%{?python_provide:%python_provide python3-jediepcserver}

%description -n python3-jediepcserver
%{summary}.


%prep
%autosetup

# Remove bundled egg-info
rm -rf *.egg-info

# Remove shebang
sed -i.orig -e 1d jediepcserver.py && \
touch -r jediepcserver.py.orig jediepcserver.py && \
rm jediepcserver.py.orig


%build
for i in %{pkg}-core.el %{pkg}.el; do
    %{_emacs_bytecompile} $i
done

%py3_build


%install
install -dm 0755 $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
install -pm 0644 %{pkg}.el* %{pkg}-core.el* setup.py -t $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
ln -s %{python3_sitelib}/jediepcserver.py $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/jediepcserver.py

install -Dpm 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_emacs_sitestartdir}/%{pkg}-init.el

%py3_install


%files
%doc CONTRIBUTING.md README.rst
%{_emacs_sitelispdir}/%{pkg}/
%{_emacs_sitestartdir}/*.el


%files -n python3-jediepcserver
%{_bindir}/jediepcserver
%pycached %{python3_sitelib}/jediepcserver.py
%{python3_sitelib}/jediepcserver-*.egg-info/


%changelog
* Tue Sep 01 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.2.8-1
- Initial RPM release
