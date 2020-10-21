Name:           rpminspect-data-fedora
Version:        1.1
Release:        2%{?dist}
Epoch:          1
Summary:        Build deviation compliance tool data files
Group:          Development/Tools
License:        CC-BY-SA
URL:            https://github.com/rpminspect/rpminspect-data-fedora
Source0:        https://github.com/rpminspect/rpminspect-data-fedora/releases/download/v1.1/rpminspect-data-fedora-1.1.tar.xz
Source1:        changelog

BuildArch:      noarch

BuildRequires:  meson

Requires:       rpminspect >= 1.1

# Used by inspections enabled in the configuration file
Requires:       xhtml1-dtds
Requires:       html401-dtds
Requires:       dash
Requires:       ksh
Requires:       zsh
Requires:       tcsh
Requires:       rc
Requires:       bash
Requires:       annobin-annocheck
Requires:       libabigail


%description
Vendor specific configuration file for rpminspect and data files used by
the inspections provided by librpminspect.


%prep
%setup -q -n rpminspect-data-fedora-1.1


%build
%meson
%meson_build


%install
%meson_install


%files
%license CC-BY-SA-4.0.txt
%doc AUTHORS README
%{_datadir}/rpminspect
%{_bindir}/rpminspect-fedora


%changelog
%include %{SOURCE1}
