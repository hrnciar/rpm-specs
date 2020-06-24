%global gnome_extensions_dir %{_datadir}/gnome-shell/extensions
%global uuid emoji-selector@maestroschan.fr

Name:           gnome-shell-extension-emoji-selector
Version:        19
Release:        2%{?dist}
Summary:        GNOME Shell extension for copying emojis to the clipboard
# The entire source code is GPLv3 except convenience.js which is BSD
License:        GPLv3 and BSD
URL:            https://github.com/maoschanz/emoji-selector-for-gnome
Source0:        %{url}/archive/%{version}/emoji-selector-%{version}.tar.gz
BuildArch:      noarch
Requires:       gnome-shell-extension-common
Recommends:     gnome-extensions-app
Recommends:     twitter-twemoji-fonts


%description
This extension provides a parametrable popup menu displaying most emojis,
clicking on an emoji copies it to the clipboard.  An appropriate font like
'Twitter Color Emoji' or 'JoyPixels Color' should be installed on your system
for a better visual result.


%prep
%autosetup -n emoji-selector-for-gnome-%{version}


%install
install -d -m 0755 %{buildroot}%{gnome_extensions_dir}

# relocate things we don't want copied into the extensions directory
mv %{uuid}/locale .
mv %{uuid}/schemas .

# install main extension files
cp -r --preserve=mode,timestamps %{uuid} %{buildroot}%{gnome_extensions_dir}

# install the schema file
install -D -p -m 0644 \
    schemas/org.gnome.shell.extensions.emoji-selector.gschema.xml \
    %{buildroot}%{_datadir}/glib-2.0/schemas/%{uuid}.gschema.xml

# install locale files
mv locale/zh{_,-}Hans
for mo in locale/*/LC_MESSAGES/*.mo; do
    install -D -p -m 0644 $mo %{buildroot}%{_datadir}/$mo
done
%find_lang emoji-selector


%files -f emoji-selector.lang
%license LICENSE
%doc README.md
%{gnome_extensions_dir}/%{uuid}
%{_datadir}/glib-2.0/schemas/%{uuid}.gschema.xml


%changelog
* Fri Jun 05 2020 Carl George <carl@george.computer> - 19-2
- Update license field

* Tue May 12 2020 Carl George <carl@george.computer> - 19-1
- Latest upstream
- Install locale files correctly

* Sun Apr 26 2020 Carl George <carl@george.computer> - 17-1
- Initial package
