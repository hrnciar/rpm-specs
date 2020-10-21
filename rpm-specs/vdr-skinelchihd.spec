%global sname   skinelchihd

Name:           vdr-skinelchihd
Version:        0.5.0
Release:        2%{?dist}
Summary:        A Elchi based skin with True Color support for the Video Disc Recorder

License:        GPLv2+
URL:            http://firefly.vdr-developer.org/skinelchihd/
Source0:        http://firefly.vdr-developer.org/%{sname}/%{name}-%{version}.tar.bz2
# Configuration files for plugin parameters. These are Fedora specific and not in upstream.
Source1:        %{name}.conf
BuildRequires:  gcc-c++
BuildRequires:  ImageMagick-c++-devel
BuildRequires:  vdr-devel >= 2.4.3
Requires:       vdr(abi)%{?_isa} = %{vdr_apiversion}

%description
This plugin for Klaus Schmidinger's Video Disc Recorder VDR adds the "Elchi HD"
skin. It is based on the Elchi skin with major re-factoring to make use of newer
VDR features like True Color support.

%prep
%autosetup -n %{sname}-%{version}

%build
%{set_build_flags}
%make_build

%install
# make install would install the themes under /etc, let's not use that
make install-lib install-i18n DESTDIR=%{buildroot}
# install the themes to the custom location used in Fedora
install -dm 755 %{buildroot}%{vdr_vardir}/themes
install -pm 644 themes/*.theme %{buildroot}%{vdr_vardir}/themes/

# skinelchihd.conf
install -Dpm 644 %{SOURCE1} \
    %{buildroot}%{_sysconfdir}/sysconfig/vdr-plugins.d/skinelchihd.conf

%find_lang %{name}

%files -f %{name}.lang
%doc HISTORY* README*
%license COPYING
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/skinelchihd.conf
%{vdr_plugindir}/libvdr-*.so.%{vdr_apiversion}
%{vdr_vardir}/themes/ElchiHD-*.theme

%changelog
* Sun Aug 30 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.5.0-2
- Install the license file with %license not %doc

* Tue Aug 25 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.5.0-1
- Initial Build
