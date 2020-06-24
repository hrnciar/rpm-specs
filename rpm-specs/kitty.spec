Name:           kitty
Version:        0.18.1
Release:        1%{?dist}
Summary:        Cross-platform, fast, feature full, GPU based terminal emulator

# Tests not passed on s390x arch
# * https://github.com/kovidgoyal/kitty/issues/2473
ExcludeArch:    s390x

# BSD:          docs/_templates/searchbox.html
# zlib:         glfw/
License:        GPLv3 and zlib and BSD
URL:            https://sw.kovidgoyal.net/kitty
Source0:        https://github.com/kovidgoyal/kitty/archive/v%{version}/%{name}-%{version}.tar.gz

# Add AppData manifest file
# * https://github.com/kovidgoyal/kitty/pull/2088
Source1:        https://raw.githubusercontent.com/kovidgoyal/kitty/46c0951751444e4f4994008f0d2dcb41e49389f4/kitty/data/%{name}.appdata.xml

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  libappstream-glib
BuildRequires:  python3-devel >= 3.6
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(zlib)

Requires:       python3%{?_isa}
Requires:       hicolor-icon-theme

# Terminfo file has been split from the main program and is required for use
# without errors. It has been separated to support SSH into remote machines using
# kitty as per the maintainers suggestion. Install the terminfo file on the remote
# machine.
Requires:       %{name}-terminfo = %{version}-%{release}

# Very weak dependencies, these are required to enable all features of kitty's
# "kittens" functions install separately
Recommends:     python3-pygments

Suggests:       ImageMagick%{?_isa}

%description
- Offloads rendering to the GPU for lower system load and buttery smooth
  scrolling. Uses threaded rendering to minimize input latency.

- Supports all modern terminal features: graphics (images), unicode, true-color,
  OpenType ligatures, mouse protocol, focus tracking, bracketed paste and
  several new terminal protocol extensions.

- Supports tiling multiple terminal windows side by side in different layouts
  without needing to use an extra program like tmux.

- Can be controlled from scripts or the shell prompt, even over SSH.

- Has a framework for Kittens, small terminal programs that can be used to
  extend kitty's functionality. For example, they are used for Unicode input,
  Hints and Side-by-side diff.

- Supports startup sessions which allow you to specify the window/tab layout,
  working directories and programs to run on startup.

- Cross-platform: kitty works on Linux and macOS, but because it uses only
  OpenGL for rendering, it should be trivial to port to other Unix-like
  platforms.

- Allows you to open the scrollback buffer in a separate window using arbitrary
  programs of your choice. This is useful for browsing the history comfortably
  in a pager or editor.

- Has multiple copy/paste buffers, like vim.


# terminfo package
%package        terminfo
Summary:        The terminfo file for Kitty Terminal
BuildArch:      noarch

Requires:       ncurses-base

%description    terminfo
Cross-platform, fast, feature full, GPU based terminal emulator.

The terminfo file for Kitty Terminal.


# doc package
%package        doc
Summary:        Documentation for %{name}

BuildRequires:  python3dist(sphinx)

%description    doc
This package contains the documentation for %{name}.


%prep
%autosetup -p1

# Replace python shebangs to make them compatible with fedora
find -type f -name "*.py" -exec sed -e 's|/usr/bin/env python3|%{__python3}|g'  \
                                    -e 's|/usr/bin/env python|%{__python3}|g'   \
                                    -i "{}" \;

# non-executable-script
sed -e "s/f.endswith('\.so')/f.endswith('\.so') or f.endswith('\.py')/g" -i setup.py

# script-without-shebang '__init__.py'
find -type f -name "*.py*" -exec chmod -x "{}"  \;


%install
%set_build_flags
%{__python3} setup.py linux-package \
    --libdir-name=%{_lib}           \
    --prefix=%{buildroot}%{_prefix} \
    --update-check-interval=0       \
    --debug
install -m 0644 -Dp %{SOURCE1} %{buildroot}%{_metainfodir}/%{name}.appdata.xml

# script-without-shebang '__init__.py'
find %{buildroot} -type f -name "*.py*" -exec chmod -x "{}"  \;

# rpmlint fixes
rm %{buildroot}%{_datadir}/doc/%{name}/html/.buildinfo \
   %{buildroot}%{_datadir}/doc/%{name}/html/.nojekyll


%check
%{__python3} setup.py test --prefix=%{buildroot}%{_prefix}
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop


%files
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*.png
%{_libdir}/%{name}/
%{_mandir}/man1/*
%{_metainfodir}/*.xml

%files terminfo
%license LICENSE
%{_datadir}/terminfo/x/xterm-%{name}

%files doc
%license LICENSE
%doc CONTRIBUTING.md CHANGELOG.rst INSTALL.md
%{_datadir}/doc/%{name}/html
%dir %{_datadir}/doc/%{name}


%changelog
* Tue Jun 23 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.18.1-1
- Update to 0.18.1

* Sat Jun 20 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.18.0-1
- Update to 0.18.0
- Disable LTO

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.17.4-2
- Rebuilt for Python 3.9

* Sat May 09 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.17.4-1
- Update to 0.17.4

* Thu Apr 23 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.17.3-1
- Update to 0.17.3

* Sun Mar 29 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.17.2-1
- Update to 0.17.2

* Tue Mar 24 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.17.1-2
- Drop sedding build flags. Not needed anymore.
- Fix build step as upstream recommended
- Do not exclude ppc64le arch anymore

* Tue Mar 24 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.17.1-1
- Update to 0.17.1

* Tue Mar 24 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.17.0-1
- Update to 0.17.0
- Exclude arch ppc64le

* Mon Mar 09 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.16.0-3
- Fix AppData description - #1811657

* Thu Mar 05 2020 Than Ngo <than@redhat.com> - 0.16.0-2
- Fixed #1792789 - kitty fails to build

* Tue Jan 28 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.16.0-1
- Update to 0.16.0

* Thu Jan 02 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.15.1-1
- Update to 0.15.1

* Wed Nov 27 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.15.0-1
- Update to 0.15.0

* Sun Oct 20 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.14.6-12
- Update to 0.14.6
- Spec file fixes
- Thanks to Vitaly Zaitsev <vitaly@easycoding.org>

* Fri Jul 12 2019 eskse <eskse@users.noreply.github.com> 0.14.2-1
- Initial version of file
