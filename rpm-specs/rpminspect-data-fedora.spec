Name:           rpminspect-data-fedora
Version:        0.10
Release:        1%{?dist}
Epoch:          1
Summary:        Build deviation compliance tool data files
Group:          Development/Tools
License:        GPLv3+
URL:            https://github.com/rpminspect/rpminspect-data-fedora
Source0:        https://github.com/rpminspect/rpminspect-data-fedora/releases/download/v0.10/rpminspect-data-fedora-0.10.tar.xz
Source1:        changelog

Provides:       rpminspect-data
Obsoletes:      rpminspect-data-generic

BuildArch:      noarch

BuildRequires:  meson

%description
Vendor specific configuration file for rpminspect and data files used by
the inspections provided by librpminspect.


%prep
%setup -q -n rpminspect-data-fedora-0.10


%build
%meson
%meson_build


%install
%meson_install


%files
%license COPYING
%doc AUTHORS README
%{_datadir}/rpminspect
%dir %{_sysconfdir}/rpminspect
%dir %{_sysconfdir}/rpminspect/profiles
%config(noreplace) %{_sysconfdir}/rpminspect/profiles/scl.conf
%config(noreplace) %{_sysconfdir}/rpminspect/rpminspect.conf


%changelog
%include %{SOURCE1}
